import json
import os
import re
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode
from urllib.request import Request, urlopen

from django.contrib.auth import authenticate, get_user_model, login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.db import IntegrityError, transaction
from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.views.decorators.http import require_GET, require_POST

from .forms import LoginForm, SignUpForm
from .models import UserProfile

TMDB_DISCOVER_URL = "https://api.themoviedb.org/3/discover/movie"


@require_GET
def home(request):
    return render(request, "index.html")


def signup(request):
    if request.user.is_authenticated:
        return redirect("home")

    form = SignUpForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        email = form.cleaned_data["email"]
        user_model = get_user_model()

        if user_model.objects.filter(email__iexact=email).exists():
            form.add_error("email", "An account with this email already exists.")
        else:
            user = user_model(
                username=email,
                email=email,
                first_name=form.cleaned_data["name"],
            )
            try:
                validate_password(form.cleaned_data["password"], user)
            except ValidationError as error:
                form.add_error("password", error)
            else:
                try:
                    with transaction.atomic():
                        user.set_password(form.cleaned_data["password"])
                        user.save()
                        UserProfile.objects.create(
                            user=user,
                            phone_number=form.cleaned_data["phone"],
                        )
                except IntegrityError:
                    form.add_error(
                        "email",
                        "An account with this email already exists.",
                    )
                else:
                    auth_login(request, user)
                    return redirect("home")

    return render(request, "movie_rating/signup.html", {"form": form})


def login_view(request):
    if request.user.is_authenticated:
        return redirect("home")

    form = LoginForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        user = authenticate(
            request,
            username=form.cleaned_data["email"],
            password=form.cleaned_data["password"],
        )
        if user is None:
            form.add_error(None, "Email or password is incorrect.")
        else:
            auth_login(request, user)
            return redirect("home")

    return render(request, "movie_rating/login.html", {"form": form})


@require_POST
def logout_view(request):
    auth_logout(request)
    return redirect("home")


@require_GET
def movies_api(request):
    try:
        page = int(request.GET.get("page", "1"))
    except ValueError:
        return JsonResponse({"error": "Page must be a number."}, status=400)

    if not 1 <= page <= 500:
        return JsonResponse({"error": "Page must be between 1 and 500."}, status=400)

    original_language = request.GET.get("original_language", "all").lower()
    if original_language != "all" and not re.fullmatch(r"[a-z]{2}", original_language):
        return JsonResponse({"error": "Language code must be a two-letter code."}, status=400)

    api_key = os.environ.get("TMDB_API_KEY")
    if not api_key:
        return JsonResponse(
            {"error": "TMDB API key is not configured. Set TMDB_API_KEY in this terminal."},
            status=503,
        )

    params = {
        "api_key": api_key,
        "language": "en-US",
        "sort_by": "popularity.desc",
        "include_adult": "false",
        "page": str(page),
    }
    if original_language != "all":
        params["with_original_language"] = original_language

    upstream_request = Request(
        f"{TMDB_DISCOVER_URL}?{urlencode(params)}",
        headers={"Accept": "application/json"},
    )

    try:
        with urlopen(upstream_request, timeout=10) as response:
            data = json.loads(response.read().decode("utf-8"))
    except HTTPError as error:
        return JsonResponse(
            {"error": f"TMDB returned HTTP {error.code}."},
            status=502,
        )
    except (URLError, TimeoutError):
        return JsonResponse({"error": "Could not connect to TMDB."}, status=502)
    except (UnicodeDecodeError, json.JSONDecodeError):
        return JsonResponse({"error": "TMDB returned invalid JSON."}, status=502)

    if not isinstance(data, dict):
        return JsonResponse({"error": "TMDB returned an invalid response."}, status=502)

    return JsonResponse(data)

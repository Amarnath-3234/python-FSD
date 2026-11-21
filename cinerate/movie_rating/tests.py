import os
from unittest.mock import MagicMock, patch
from urllib.parse import parse_qs, urlparse

from django.contrib.auth import get_user_model
from django.test import TestCase


class MoviesApiTests(TestCase):
    def test_missing_api_key_returns_configuration_error(self):
        with patch.dict(os.environ, {"TMDB_API_KEY": ""}):
            response = self.client.get("/api/movies/")

        self.assertEqual(response.status_code, 503)
        self.assertIn("TMDB_API_KEY", response.json()["error"])

    def test_proxy_passes_filters_without_returning_api_key(self):
        upstream_response = MagicMock()
        upstream_response.__enter__.return_value = upstream_response
        upstream_response.read.return_value = b'{"page":2,"results":[]}'

        with (
            patch.dict(os.environ, {"TMDB_API_KEY": "test-key"}),
            patch("movie_rating.views.urlopen", return_value=upstream_response) as mocked_urlopen,
        ):
            response = self.client.get(
                "/api/movies/?page=2&original_language=ta"
            )

        self.assertEqual(response.status_code, 200)
        self.assertNotIn("api_key", response.json())

        upstream_url = mocked_urlopen.call_args.args[0].full_url
        query = parse_qs(urlparse(upstream_url).query)
        self.assertEqual(query["api_key"], ["test-key"])
        self.assertEqual(query["page"], ["2"])
        self.assertEqual(query["with_original_language"], ["ta"])

    def test_rejects_out_of_range_page(self):
        response = self.client.get("/api/movies/?page=501")

        self.assertEqual(response.status_code, 400)


class AccountAuthTests(TestCase):
    def test_signup_creates_account_and_logs_user_in(self):
        response = self.client.post(
            "/signup/",
            {
                "name": "Avery Smith",
                "email": "AVERY@example.com",
                "password": "RiverMovie!2026",
                "phone": "+1 555 123 4567",
            },
        )

        self.assertRedirects(response, "/")
        user = get_user_model().objects.get(email="avery@example.com")
        self.assertTrue(user.check_password("RiverMovie!2026"))
        self.assertEqual(user.profile.phone_number, "+1 555 123 4567")
        self.assertEqual(
            self.client.session["_auth_user_id"],
            str(user.pk),
        )

    def test_login_accepts_email_case_insensitively(self):
        get_user_model().objects.create_user(
            username="viewer@example.com",
            email="viewer@example.com",
            password="RiverMovie!2026",
        )

        response = self.client.post(
            "/login/",
            {
                "email": "VIEWER@example.com",
                "password": "RiverMovie!2026",
            },
        )

        self.assertRedirects(response, "/")

    def test_login_rejects_incorrect_password(self):
        get_user_model().objects.create_user(
            username="viewer@example.com",
            email="viewer@example.com",
            password="RiverMovie!2026",
        )

        response = self.client.post(
            "/login/",
            {
                "email": "viewer@example.com",
                "password": "incorrect",
            },
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Email or password is incorrect.")

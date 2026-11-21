from django import forms
from django.core.validators import RegexValidator


class SignUpForm(forms.Form):
    name = forms.CharField(
        max_length=150,
        widget=forms.TextInput(attrs={"autocomplete": "name"}),
    )
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={"autocomplete": "email", "placeholder": "you@gmail.com"}
        ),
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
    )
    phone = forms.CharField(
        max_length=20,
        validators=[
            RegexValidator(
                r"^\+?[0-9 ()-]{7,20}$",
                "Enter a valid phone number.",
            )
        ],
        widget=forms.TextInput(
            attrs={"autocomplete": "tel", "type": "tel"}
        ),
    )

    def clean_email(self):
        return self.cleaned_data["email"].strip().lower()

    def clean_phone(self):
        return self.cleaned_data["phone"].strip()


class LoginForm(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={"autocomplete": "email"}),
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"autocomplete": "current-password"}),
    )

    def clean_email(self):
        return self.cleaned_data["email"].strip().lower()

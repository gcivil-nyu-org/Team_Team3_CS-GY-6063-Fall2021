from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text="Required")

    def clean_email(self):
        if User.objects.filter(email=self.cleaned_data["email"]).exists():
            raise forms.ValidationError("The given email is already registered")
        return self.cleaned_data["email"]

    class Meta:
        model = User
        fields = (
            "username",
            "email",
            "first_name",
            "last_name",
            "password1",
            "password2",
        )

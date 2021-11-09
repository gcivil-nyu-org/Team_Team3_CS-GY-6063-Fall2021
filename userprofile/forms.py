from django import forms
from .models import Profile
from django.contrib.auth.models import User


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username"]


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            "profilename",
            "image",
            "bocce",
            "frisbee",
            "adultBaseball",
            "adultFootball",
            "adultSoftball",
            "basketball",
            "cricket",
            "flagFootball",
            "handball",
            "hockey",
            "kickball",
            "lacrosse",
            "netball",
            "rugby",
            "tennis",
            "volleyball",
            "hiking",
            "location",
            "distance",
            "car",
        ]

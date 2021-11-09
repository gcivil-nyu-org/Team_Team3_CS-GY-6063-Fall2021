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
            "tBall",
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
            "littleLeagueBaseball",
            "littleLeagueSoftball",
            "netball",
            "rugby",
            "tennis",
            "volleyball",
            "youthFootball",
            "hiking",
            "location",
            "distance",
            "car",
        ]

class UserDeleteProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = []

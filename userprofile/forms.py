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
            "baseball",
            "basketball",
            "cricket",
            "flagFootball",
            "football",
            "handball",
            "hockey",
            "kickball",
            "lacrosse",
            "netball",
            "rugby",
            "softball",
            "tennis",
            "volleyball",
            "hiking",
            "location",
            "distance",
            "car",
        ]
        
class UserDeleteProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = []
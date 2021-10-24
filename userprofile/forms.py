from django import forms
from .models import Profile

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profilename','bocce','frisbee','tBall','adultBaseball','adultFootball','adultSoftball','basketball',
        'cricket','flagFootball','handball','hockey','kickball','lacrosse','littleLeagueBaseball','littleLeagueSoftball',
        'netball','rugby','tennis','volleyball','youthFootball','hiking','location','distance','car']
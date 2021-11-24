from django import forms
from django.contrib.auth.models import User
from .models import Noshow,Misbehavior


class ReportNoShowForm(forms.ModelForm):
  class Meta:
    model = Noshow
    fields = ['name', 'description']

class ReportMisbehaviorForm(forms.ModelForm):
  class Meta:
    model = Misbehavior
    fields = ['name', 'description']
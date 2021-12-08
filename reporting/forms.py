from django import forms
from .models import Noshow,Misbehavior
from django.contrib.auth.models import User


class ReportNoShowForm(forms.ModelForm):
  class Meta:
    model = Noshow
    fields = ['name', 'description']

  def __init__(self, *args, **kwargs):
        user = kwargs.pop('user',None)
        super(ReportNoShowForm,self).__init__(*args, **kwargs)
        self.fields['name'].queryset = User.objects.filter().exclude(username=user)

class ReportMisbehaviorForm(forms.ModelForm):
  class Meta:
    model = Misbehavior
    fields = ['name', 'description']

  def __init__(self, *args, **kwargs):
        user = kwargs.pop('user',None)
        super(ReportMisbehaviorForm,self).__init__(*args, **kwargs)
        self.fields['name'].queryset = User.objects.filter().exclude(username=user)

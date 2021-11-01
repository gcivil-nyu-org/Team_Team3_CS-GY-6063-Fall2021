from django.forms import widgets
from django.shortcuts import render
from .models import Event
from django.views.generic import (
  CreateView,
  ListView, 
  DetailView
  )
from django import forms

# Create your views here.
def event(request):
  context = {
    'event': Event.objects.all().last()
  }

  return render(request, "events/event.html", context)

class EventsListView(ListView):
  model = Event
  template_name = 'events/events_list.html'
  context_object_name = 'events'
  ordering=['-dateCreated']

class EventDetailView(DetailView):
  model = Event
  template_name = 'events/events_detail.html'

class DateInput(forms.DateTimeInput):
  input_type='datetime-local'

class CreateEventForm(forms.ModelForm):
  class Meta:
    model = Event
    fields = ['name', 'description', 'address', 'date']
    widgets = {'date' : DateInput()}

class EventsCreateView(CreateView):
  form_class = CreateEventForm
  model = Event

  def form_valid(self, form):
    form.instance.owner = self.request.user
    form.instance.locationId = self.kwargs.get('id', None)
    return super().form_valid(form)



def add_event(request, id):
  return render(request, "events/add_event.html", {"id": id})

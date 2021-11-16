from django.contrib.auth.decorators import login_required
from .models import Event, EventRegistration
from django.shortcuts import redirect 
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
  CreateView,
  ListView, 
  DetailView,
  UpdateView,
  DeleteView
  )
from django.core.exceptions import ValidationError
from django import forms
from django.utils import timezone
from datetime import timedelta
from maps.facilities_data import read_facilities_data, read_hiking_data
import json


class EventsListView(ListView):
  model = Event
  template_name = 'events/events_list.html'
  context_object_name = 'events'
  ordering=['-dateCreated']

class EventDetailView(DetailView):
  model = Event
  template_name = 'events/events_detail.html'

  def get_context_data(self, **kwargs):
    isAttending = False
    context = super(EventDetailView, self).get_context_data(**kwargs)
    context['attendees'] = EventRegistration.objects.filter(event = context["object"]);
    for attendee in context['attendees']:
      if attendee.user == self.request.user:
        isAttending = True
    context['isAttending'] = isAttending
    context['isOwner'] = self.object.owner == self.request.user
    date = self.object.date - timedelta(hours =2) 
    context['canDelete'] = date > timezone.now()
    return context

@login_required
def event_add_attendance(request, pk):
  this_event = Event.objects.get(pk=pk)
  this_event.add_user_to_list_of_attendees(user=request.user)
  return redirect("event-detail", pk)

@login_required
def event_cancel_attendance(request, pk):
  this_event = Event.objects.get(pk=pk)
  this_event.remove_user_from_list_of_attendees(request.user)
  return redirect("event-detail", pk)

class DateInput(forms.DateTimeInput):
  input_type='datetime-local'

class CreateEventForm(forms.ModelForm):
  class Meta:
    model = Event
    fields = ['name', 'description', 'address', 'date', 'numberOfPlayers']
    widgets = {'date' : DateInput()}

class UpdateEventForm(forms.ModelForm):
  class Meta:
    model = Event
    fields = ['name', 'description', 'address', 'date', 'numberOfPlayers']
    widgets = {'date' : DateInput()}

def get_sport_key(sport):
  return {
  'Bocce': 'bocce',
  'Track': "track_and",
  'Frisbee':"frisbee",
  'Baseball': "adult_base",
  'Football': "adult_foot",
  'Softball': "adult_soft",
  'Basketball': "basketball",
  'Cricket': "cricket",
  'Flag Football': "flagfootba",
  'Handball': "handball",
  'Hockey': "hockey",
  'Kickball': "kickball",
  'Lacrosse': "lacrosse",
  'Netball': "netball",
  'Rugby': "rugby",
  'Tennis':"tennis",
  'Volleyball': "volleyball"
  }[sport]
class EventsCreateView(LoginRequiredMixin, CreateView):
  form_class = CreateEventForm
  model = Event
    
  def form_valid(self, form):
    form.instance.owner = self.request.user
    form.instance.locationId = self.kwargs.get('id', None)
    form.instance.sport = self.kwargs.get('sport', None)
    data =  json.loads(read_hiking_data()) if self.kwargs.get('sport', None) == 'Hiking' else json.loads(read_facilities_data())

    if self.kwargs.get('sport', None) != 'Hiking':
      currentFacility = data[str(self.kwargs.get('id', None))]

      sportIsAvailable = currentFacility[get_sport_key(str(self.kwargs.get('sport', None)))]
      if sportIsAvailable != 'Yes':
        raise ValidationError(
          str(self.kwargs.get('sport', None)) + " is not available at this facility."
        )
    
      borough = currentFacility['borough']

      if borough == 'B':
        form.instance.borough = 'Brooklyn'
      elif borough == 'M':
        form.instance.borough = 'Manhattan'
      elif borough == 'X':
        form.instance.borough = 'Bronx'
      elif borough == 'R':
        form.instance.borough = 'Staten Island'
      else:
        form.instance.borough = 'Queens'
    return super().form_valid(form)

class EventUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
  form_class = UpdateEventForm
  model = Event

  def form_valid(self, form):
    form.instance.owner = self.request.user
    return super().form_valid(form)

  def test_func(self):
    event = self.get_object()
    if self.request.user == event.owner:
      return True
    return False

class EventDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
  model = Event
  template_name = 'events/event_confirm_delete.html'
  success_url = '/'

  def test_func(self):
    event = self.get_object()
    if self.request.user == event.owner:
      return True
    return False



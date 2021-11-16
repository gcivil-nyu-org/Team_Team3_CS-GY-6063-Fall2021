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
from django import forms
from maps.facilities_data import read_facilities_data
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
    fields = ['name', 'description', 'address', 'date']
    widgets = {'date' : DateInput()}

class UpdateEventForm(forms.ModelForm):
  class Meta:
    model = Event
    fields = ['name', 'description', 'address', 'locationId', 'date']
    date = forms.DateField(widget=DateInput(), initial=DateInput())

class EventsCreateView(LoginRequiredMixin, CreateView):
  form_class = CreateEventForm
  model = Event

  def form_valid(self, form):
    form.instance.owner = self.request.user
    form.instance.locationId = self.kwargs.get('id', None)
    data = json.loads(read_facilities_data())
    currentFacility = data[str(self.kwargs.get('id', None))]
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


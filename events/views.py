from django.contrib.auth.decorators import login_required
from .models import Event, EventRegistration
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse
from django.views.generic import (
  CreateView,
  ListView, 
  DetailView,
  UpdateView,
  DeleteView
  )
from django.core.exceptions import ValidationError
from django import forms
from datetime import timedelta
from django.utils import timezone
from maps.facilities_data import read_facilities_data, read_hiking_data
import json
from django.contrib import messages
from django.contrib.auth.models import User
from django.db.models import Q
from userprofile.models import Profile
import random
from .filters import EventFilter
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMultiAlternatives
from config.settings import EMAIL_HOST_USER


class EventsListView(ListView):
  model = Event
  template_name = 'events/events_list.html'
  context_object_name = 'events'
  ordering=['-dateCreated']

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    now = timezone.now()
    context["filter"] = EventFilter(self.request.GET, queryset=self.get_queryset().filter(date__gte=now))

    
    return context
  

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
    updateTime = self.object.date - timedelta(hours =24)
    unjoinTime = self.object.date - timedelta(hours =2)
    context['canUpdate'] = updateTime > timezone.now()
    context['canUnjoin'] = unjoinTime > timezone.now()
    
    return context

@login_required
def event_add_attendance(request, pk):
  this_event = Event.objects.get(pk=pk)
  num_registered = this_event.get_registrations().count()
  if num_registered == this_event.numberOfPlayers:
    messages.success(request, 'Event Already Full!')
    return redirect("event-detail", pk)
    
  this_event.add_user_to_list_of_attendees(user=request.user)
  
  new_num_registered = this_event.get_registrations().count()
  if new_num_registered == this_event.numberOfPlayers:
    attendees = this_event.get_registrations()
    sport = this_event.sport
    for x in attendees:
      user = User.objects.get(username=x)
      to = user.email
      subject = 'Squad Ready'
      text_content = 'Hi' + str(user) + '! Your squad has been formed for a ' + str(sport.lower()) +  ' event.'
      link = str(get_current_site(request)) + '/events/' + str(this_event.pk)
      html_content = '<p> Hi ' + str(user) + '! Your squad has been formed for a <strong>' + str(sport.lower()) +  '</strong> event.</p> <a href="http://' + str(link) + '/">See Event Details</a>'
      msg = EmailMultiAlternatives(subject, text_content, EMAIL_HOST_USER, [to])
      msg.attach_alternative(html_content, "text/html")
      msg.send() 
  
  return redirect("event-detail", pk)

@login_required
def event_cancel_attendance(request, pk):
  this_event = Event.objects.get(pk=pk)
  borough = this_event.borough
  sport = this_event.sport
  num_registered = this_event.get_registrations().count()
  if num_registered == this_event.numberOfPlayers:
    this_event.remove_user_from_list_of_attendees(request.user)
    attendees = this_event.get_registrations()
    for x in attendees:
      user = User.objects.get(username=x) 
      to = user.email
      subject = 'Squad Opening'
      text_content = 'Hi' + str(user) + '! There is an open spot for your upcoming ' + str(sport.lower()) +  ' event.'
      link = str(get_current_site(request)) + '/events/' + str(this_event.pk)
      html_content = '<p> Hi ' + str(user) + '! There is an open spot for your upcoming <strong>' + str(sport.lower()) +  '</strong> event.</p> <a href="http://' + str(link) + '/">See Event Details</a>'
      msg = EmailMultiAlternatives(subject, text_content, EMAIL_HOST_USER, [to])
      msg.attach_alternative(html_content, "text/html")
      msg.send()  
  else:
    this_event.remove_user_from_list_of_attendees(request.user)

  if timezone.now() + timedelta(hours=24, minutes=0) > this_event.date:
    interested_users = Profile.objects.filter((Q(distance__contains=borough.upper()) | Q(location=borough.lower())), **{sport.lower(): True})
    attendees = this_event.get_registrations()
    int_users_list = list(interested_users.values('user_id'))
    attendees_list = list(attendees.values('user_id'))
    attendees_list.append({'user_id':request.user.pk})

    notification_list = [i for i in int_users_list if i not in attendees_list]

    if 0 < len(notification_list) < 21:
      for x in notification_list:
        user = User.objects.get(pk=x["user_id"])
        to = user.email
        subject = 'Upcoming Event'
        text_content = 'Hi' + str(user) + '! There is an upcoming ' + str(sport.lower()) +  ' event you may be interested in.'
        link = str(get_current_site(request)) + '/events/' + str(this_event.pk)
        html_content = '<p> Hi ' + str(user) + '! There is an upcoming <strong>' + str(sport.lower()) +  '</strong> event you may be interested in.</p> <a href="http://' + str(link) + '/">Learn more about this event.</a>'
        msg = EmailMultiAlternatives(subject, text_content, EMAIL_HOST_USER, [to])
        msg.attach_alternative(html_content, "text/html")
        msg.send()    
    elif len(notification_list) > 20:
      random_users = random.sample(notification_list, 20)
      for x in random_users:
        user = User.objects.get(pk=x["user_id"])
        to = user.email
        subject = 'Upcoming Event'
        text_content = 'Hi' + str(user) + '! There is an upcoming ' + str(sport.lower()) +  ' event you may be interested in.'
        link = str(get_current_site(request)) + '/events/' + str(this_event.pk)
        html_content = '<p> Hi ' + str(user) + '! There is an upcoming <strong>' + str(sport.lower()) +  '</strong> event you may be interested in.</p> <a href="http://' + str(link) + '/">Learn more about this event.</a>'
        msg = EmailMultiAlternatives(subject, text_content, EMAIL_HOST_USER, [to])
        msg.attach_alternative(html_content, "text/html")
        msg.send() 

  return redirect("event-detail", pk)

class DateInput(forms.DateTimeInput):
  input_type='datetime-local'

class CreateEventForm(forms.ModelForm):
  class Meta:
    model = Event
    fields = ['name', 'description', 'date', 'numberOfPlayers']
    widgets = {'date' : DateInput()}

class UpdateEventForm(forms.ModelForm):
  class Meta:
    model = Event
    fields = ['name', 'description', 'date', 'numberOfPlayers']
    date = forms.DateField(widget=DateInput(), initial=DateInput())

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

    current_id = self.kwargs.get('id', None)

    if Event.objects.filter(owner=self.request.user, locationId=current_id, name=self.request.POST.get('name'),date=self.request.POST.get('date')).count() > 0:
      messages.success(self.request, 'A similar event already exists!')
      return redirect(reverse("add-event", kwargs={'sport':self.kwargs.get('sport', None),'id': current_id}))

    if self.kwargs.get('sport', None) != 'Hiking':
      if str(current_id) in self.request.session:

        saved_address = self.request.session[str(current_id)]
        
        form.instance.address = str(saved_address)
      
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

    elif self.kwargs.get('sport', None) == 'Hiking':
      if 1 <= int(current_id) <= 37: 
        currentTrail = data[str(self.kwargs.get('id', None))]
        park = currentTrail['Park_Name']
        form.instance.address = park
      else:
        raise ValidationError(
          "Invalid location id"
        )
    return super().form_valid(form)
  
  def get_success_url(self):
    return reverse('join-event', kwargs={'pk': self.object.pk})



class EventUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
  form_class = UpdateEventForm
  model = Event

  def form_valid(self, form):
    form.instance.owner = self.request.user
    return super().form_valid(form)

  def test_func(self):
    event = self.get_object();
    updateTime = event.date - timedelta(hours =24)
    canUpdate = updateTime > timezone.now()
    if self.request.user == event.owner and canUpdate:
      return True
    return False

class EventDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
  model = Event
  template_name = 'events/event_confirm_delete.html'
  success_url = '/'

  def test_func(self):
    event = self.get_object()
    updateTime = event.date - timedelta(hours =24)
    canUpdate = updateTime > timezone.now()
    if self.request.user == event.owner and canUpdate:
      return True
    return False



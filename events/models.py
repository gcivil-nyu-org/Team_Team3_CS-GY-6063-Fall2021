from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.core.exceptions import ValidationError
from datetime import timedelta


@property
def is_past_due(self):
    return timezone.now() > self.date

class Event(models.Model):
  def no_past(value):
    if value < timezone.now():
      raise ValidationError("The date cannot be in the past!")

  def more_than_3hrs(value):
    if (timezone.now() + timedelta(hours=2,minutes=59) > value) and value > timezone.now():
      raise ValidationError("Cannot create an event within 3hrs!")

  name = models.CharField(max_length=100)
  description = models.TextField()
  address = models.TextField()
  locationId = models.CharField(max_length=100)
  date = models.DateTimeField(verbose_name="Event Date", validators=[no_past,more_than_3hrs])
  dateCreated = models.DateTimeField(default=timezone.now)
  owner = models.ForeignKey(User, on_delete=models.CASCADE)
  borough = models.CharField(max_length=20)
  sport = models.CharField(max_length=30)
  numberOfPlayers = models.PositiveIntegerField("Number of People Needed:")

  def clean(self, *args, **kwargs):
    if self.date < timezone.now():
      raise ValidationError("The date cannot be in the past!")
      
    if self.numberOfPlayers <= 1:
      raise ValidationError("Enter a number greater than 1!")
    super(Event, self).clean(*args, **kwargs)
    
  class Meta:
        verbose_name = "event"
        verbose_name_plural = "events"

  def get_registrations(self):
    return EventRegistration.objects.filter(event = self)

  def add_user_to_list_of_attendees(self, user):
    registration = EventRegistration.objects.create(user = user,  event = self, time_registered = timezone.now())
    return registration

  def remove_user_from_list_of_attendees(self, user):
      registration = EventRegistration.objects.get(user = user, event = self)
      registration.delete()
      return True

  def get_absolute_url(self):
    return reverse("event-detail", kwargs={"pk": self.pk})

class EventRegistration(models.Model):
    event = models.ForeignKey(Event,verbose_name='Event', on_delete=models.CASCADE)
    user = models.ForeignKey(User,verbose_name='Attendee', on_delete=models.CASCADE)
    time_registered = models.DateTimeField()
    def __str__(self):
      return self.user.username

    class Meta:
      verbose_name = 'Attendee for event'
      verbose_name_plural = 'Attendees for events'
      ordering = ['time_registered']
      unique_together = ('event', 'user')

    def save(self, *args, **kwargs):
      if self.id is None and self.time_registered is None:
        self.time_registered = timezone.now()
      super(EventRegistration, self).save(*args, **kwargs)

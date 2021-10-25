
from django.db import models
from django.contrib.auth.models import User


class Event(models.Model):
	name = models.CharField('Event Name', max_length=120)
	event_date = models.DateTimeField('Event Date')
	location = models.TextField('Event Name', max_length=500)
	creator = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)
	description = models.TextField(blank=True)
	attendees = models.ManyToManyField(User, blank=True)

	def __str__(self):
		return self.name
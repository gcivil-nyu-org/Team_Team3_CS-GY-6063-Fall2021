from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Event(models.Model):
  name = models.CharField(max_length=100);
  description = models.TextField();
  address = models.TextField();
  locationId = models.CharField(max_length=100);
  date = models.DateTimeField();
  dateCreated = models.DateTimeField(default=timezone.now)
  owner = models.ForeignKey(User, on_delete=models.DO_NOTHING);

  def get_absolute_url(self):
      return reverse("event-detail", kwargs={"pk": self.pk})
  
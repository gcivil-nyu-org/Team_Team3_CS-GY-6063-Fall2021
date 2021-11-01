from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Event(models.Model):
  name = models.CharField(max_length=100);
  description = models.TextField();
  address = models.TextField();
  locationId = models.CharField(max_length=100);
  date = models.DateTimeField();
  owner = models.ForeignKey(User, on_delete=models.DO_NOTHING);

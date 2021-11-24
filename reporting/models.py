from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Noshow(models.Model):
  owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='+')
  name = models.ForeignKey(User, on_delete=models.CASCADE, related_name='+')
  description = models.TextField()
  date = models.DateTimeField(default=timezone.now)


class Misbehavior(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='+')
  name = models.ForeignKey(User, on_delete=models.CASCADE,related_name='+')
  description = models.TextField()
  date = models.DateTimeField(default=timezone.now)

  
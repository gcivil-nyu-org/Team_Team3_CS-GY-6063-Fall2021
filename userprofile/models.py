from django.db import models
from django.contrib.auth.models import User

    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profilename = models.CharField(default= 'Outdoor Squad Member', max_length=50)
    bocce = models.BooleanField(default=False)
    frisbee = models.BooleanField(default=False)
    tBall = models.BooleanField(default=False)
    adultBaseball = models.BooleanField(default=False)
    adultFootball = models.BooleanField(default=False)
    adultSoftball = models.BooleanField(default=False)
    basketball = models.BooleanField(default=False)
    cricket = models.BooleanField(default=False)
    flagFootball = models.BooleanField(default=False)
    handball = models.BooleanField(default=False)
    hockey = models.BooleanField(default=False)
    kickball = models.BooleanField(default=False)
    lacrosse = models.BooleanField(default=False)
    littleLeagueBaseball = models.BooleanField(default=False)
    littleLeagueSoftball = models.BooleanField(default=False)
    netball = models.BooleanField(default=False)
    rugby = models.BooleanField(default=False)
    tennis = models.BooleanField(default=False)
    volleyball = models.BooleanField(default=False)
    youthFootball = models.BooleanField(default=False)
    hiking = models.BooleanField(default=False)
    location = models.CharField(default ='NYC', max_length=50)
    distance = models.IntegerField(default=0)
    car = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)


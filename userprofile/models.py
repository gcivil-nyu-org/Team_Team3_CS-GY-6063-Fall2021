from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from multiselectfield import MultiSelectField
# from django.core.files.storage import default_storage as storage


LOCATION_CHOICES = (
    ("select", "SELECT"),
    ("manhattan", "MANHATTAN"),
    ("queens", "QUEENS"),
    ("bronx", "BRONX"),
    ("brooklyn", "BROOKLYN"),
    ("staten_island", "STATEN ISLAND"),
)

BOROUGH_CHOICES = (
    ("manhattan", "MANHATTAN"),
    ("queens", "QUEENS"),
    ("bronx", "BRONX"),
    ("brooklyn", "BROOKLYN"),
    ("staten_island", "STATEN ISLAND"),
)

CAR = (
    ("select", "SELECT"),
    ("yes", "YES"),
    ("no", "NO"),
)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profilename = models.CharField(default="Outdoor Squad Member", max_length=50)
    image = models.ImageField(default="default.jpg", upload_to="profile_pics")
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
    location = models.CharField(
        verbose_name="Borough",
        max_length=20,
        choices=LOCATION_CHOICES,
        default="select",
    )
    distance = MultiSelectField(
        verbose_name="Boroughs Willing to Travel:",
        choices=BOROUGH_CHOICES,
        max_choices=5,
        blank=True,
    )
    car = models.CharField(max_length=10, choices=CAR, default="select")

    def __str__(self):
        return f"{self.user.username} Profile"

    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)

        img = Image.open(self.image.name)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.name)

        # x = self.cleaned_data.get('x')
        # y = self.cleaned_data.get('y')
        # w = self.cleaned_data.get('width')
        # h = self.cleaned_data.get('height')

        # image = Image.open(self.image.path)
        # cropped_image = image.crop((x, y, w + x, h + y))
        # resized_image = cropped_image.resize((200, 200), Image.ANTIALIAS)

        # fh = storage.open(self.image.path, "wb")
        # picture_format = 'png'
        # resized_image.save(fh, picture_format)
        # fh.close()        
        # return user
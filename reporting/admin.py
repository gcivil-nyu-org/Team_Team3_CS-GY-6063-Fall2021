from django.contrib import admin
from .models import Noshow,Misbehavior

# Register your models here.

admin.site.register(Noshow);
admin.site.register(Misbehavior);

from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
  path("created/", views.event, name="event"),
  path("add/<int:id>", views.add_event, name="add-event"),
]

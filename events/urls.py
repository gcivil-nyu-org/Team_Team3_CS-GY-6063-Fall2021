from django.urls import path

from . import views

urlpatterns = [
    path("events/add_event", views.add_event, name="add_event"),
]

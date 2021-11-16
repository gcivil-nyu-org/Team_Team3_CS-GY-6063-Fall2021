from django.urls import path

from . import views

urlpatterns = [
    path("squad", views.squad, name="squad"),
]

from django.urls import path

from . import views

urlpatterns = [
    path("<int:id>/<address>", views.show, name="show"),
    path("trails/<int:id>", views.trails, name="trails"),
]

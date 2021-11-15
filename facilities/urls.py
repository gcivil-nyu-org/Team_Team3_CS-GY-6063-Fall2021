from django.urls import path

from . import views

urlpatterns = [
    path("<str:sport>/<int:id>", views.show, name="show"),
    path("trails/<int:id>", views.trails, name="trails"),
]

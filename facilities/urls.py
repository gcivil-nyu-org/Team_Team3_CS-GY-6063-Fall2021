from django.urls import path

from . import views

urlpatterns = [
    path("<int:id>", views.show, name="show"),
    path("<str:sport>/<int:id>", views.showWithSport, name="show-with-sport"),
    path("hiking/trails/<int:id>", views.trails, name="trails"),
]

from django.conf.urls import url
from . import views

urlpatterns = [
    url("edit_profile", views.profile, name="profile_edit"),
    url("profile", views.profile_page, name="profile_page"),
    url("delete", views.delete_profile, name="profile_delete"),
]

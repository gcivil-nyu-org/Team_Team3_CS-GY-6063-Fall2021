from django.conf.urls import url
from . import views

urlpatterns = [
    url("contact_us", views.ContactUs, name="contact_us"),
    url("report_noshow", views.no_show, name="report_noshow"),
    url("report_misbehavior", views.misbehavior, name="report_misbehavior"),
]
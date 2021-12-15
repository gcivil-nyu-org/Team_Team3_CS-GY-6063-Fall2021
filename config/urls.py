"""congif URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# config/urls.py
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.base import TemplateView
from config.views import HomePageView
from accounts.forms import EmailValidationOnForgotPassword

urlpatterns = [
    path("admin/", admin.site.urls),
    path(
        "accounts/password_reset/",
        auth_views.PasswordResetView.as_view(
            form_class=EmailValidationOnForgotPassword
        ),
        name="password_reset",
    ),
    path("accounts/", include("accounts.urls")),
    path("accounts/", include("django.contrib.auth.urls")),
    path("", HomePageView.as_view(template_name="home.html"), name="home"),  # new
    path("about", TemplateView.as_view(template_name="about.html"), name="about"),
    path(
        "accounts/signup/",
        TemplateView.as_view(template_name="signup.html"),
        name="signup",
    ),  # new
    path("maps/", include("maps.urls")),
    path("facilities/", include("facilities.urls")),
    path("events/", include("events.urls")),
    path("userprofile/", include("userprofile.urls")),
    path("", include("squad.urls")),
    path("messaging/", include("messaging.urls")),
    path("reporting/", include("reporting.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.conf.urls import url
from . import views

urlpatterns = [
    # url(r'^$', views.home, name='home'),
    url(r"^signup/$", views.signup, name="signup"),
    # needed to update match repetitions
    url(
        r"^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,6}-[0-9A-Za-z]{1,32})/$",
        views.activate,
        name="activate",
    ),
]

from django.conf.urls import url                                                                                                                              
from . import views

urlpatterns = [ 
    url(r'^maps/', views.default_map, name="maps"),
]
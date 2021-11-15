from django.conf.urls import url

from . import views

urlpatterns = [
    url("map", views.default_map, name="default_map"),
    url("basketball", views.activity_map, name="basketball"),
    url("baseball", views.activity_map, name="baseball"),
    url("netball", views.activity_map, name="netball"),
    url("softball", views.activity_map, name="softball"),
    url("kickball", views.activity_map, name="kickball"),
    url("handball", views.activity_map, name="handball"),
    url("bocce", views.activity_map, name="bocce"),
    url("frisbee", views.activity_map, name="frisbee"),
    url("rugby", views.activity_map, name="rugby"),
    url("cricket", views.activity_map, name="cricket"),
    url("hockey", views.activity_map, name="hockey"),
    url("volleyball", views.activity_map, name="volleyball"),
    url("flag_football", views.activity_map, name="flag_football"),
    url("tennis", views.activity_map, name="tennis"),
    url("lacrosse", views.activity_map, name="lacrosse"),
    url("football", views.activity_map, name="football"),
    url("hiking", views.hiking_map, name="hiking"),
]

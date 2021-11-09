from django.conf.urls import url

from . import views

urlpatterns = [
    url("map", views.default_map, name="default_map"),
    url("basketball", views.basketball_map, name="basketball_map"),
    url("baseball", views.baseball_map, name="baseball_map"),
    url("netball", views.netball_map, name="netball_map"),
    url("softball", views.softball_map, name="softball_map"),
    url("kickball", views.kickball_map, name="kickball_map"),
    url("handball", views.handball_map, name="handball_map"),
    url("bocce", views.bocce_map, name="bocce_map"),
    url("frisbee", views.frisbee_map, name="frisbee_map"),
    url("rugby", views.rugby_map, name="rugby_map"),
    url("cricket", views.cricket_map, name="cricket_map"),
    url("hockey", views.hockey_map, name="hockey_map"),
    url("volleyball", views.volleyball_map, name="volleyball_map"),
    url("flag_football", views.flag_football_map, name="flag_football_map"),
    url("tennis", views.tennis_map, name="tennis_map"),
    url("lacrosse", views.lacrosse_map, name="lacrosse_map"),
    url("football", views.football_map, name="football_map"),
    url("hiking", views.hiking_map, name="hiking_map"),
]

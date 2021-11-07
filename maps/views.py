from django.shortcuts import render
from config.settings import MAPBOX_TOKEN


def default_map(request):
    mapbox_access_token = MAPBOX_TOKEN
    return render(
        request, "maps/map.html", {"mapbox_access_token": mapbox_access_token}
    )


def basketball_map(request):
    mapbox_access_token = MAPBOX_TOKEN
    return render(
        request, "maps/basketball.html", {"mapbox_access_token": mapbox_access_token}
    )


def baseball_map(request):
    mapbox_access_token = MAPBOX_TOKEN
    return render(
        request, "maps/baseball.html", {"mapbox_access_token": mapbox_access_token}
    )


def handball_map(request):
    mapbox_access_token = MAPBOX_TOKEN
    return render(
        request, "maps/handball.html", {"mapbox_access_token": mapbox_access_token}
    )


def kickball_map(request):
    mapbox_access_token = MAPBOX_TOKEN
    return render(
        request, "maps/kickball.html", {"mapbox_access_token": mapbox_access_token}
    )


def bocce_map(request):
    mapbox_access_token = MAPBOX_TOKEN
    return render(
        request, "maps/bocce.html", {"mapbox_access_token": mapbox_access_token}
    )


def frisbee_map(request):
    mapbox_access_token = MAPBOX_TOKEN
    return render(
        request, "maps/frisbee.html", {"mapbox_access_token": mapbox_access_token}
    )


def flag_football_map(request):
    mapbox_access_token = MAPBOX_TOKEN
    return render(
        request, "maps/flag_football.html", {"mapbox_access_token": mapbox_access_token}
    )


def rugby_map(request):
    mapbox_access_token = MAPBOX_TOKEN
    return render(
        request, "maps/rugby.html", {"mapbox_access_token": mapbox_access_token}
    )


def cricket_map(request):
    mapbox_access_token = MAPBOX_TOKEN
    return render(
        request, "maps/cricket.html", {"mapbox_access_token": mapbox_access_token}
    )


def tennis_map(request):
    mapbox_access_token = MAPBOX_TOKEN
    return render(
        request, "maps/tennis.html", {"mapbox_access_token": mapbox_access_token}
    )


def hockey_map(request):
    mapbox_access_token = MAPBOX_TOKEN
    return render(
        request, "maps/hockey.html", {"mapbox_access_token": mapbox_access_token}
    )


def lacrosse_map(request):
    mapbox_access_token = MAPBOX_TOKEN
    return render(
        request, "maps/lacrosse.html", {"mapbox_access_token": mapbox_access_token}
    )


def netball_map(request):
    mapbox_access_token = MAPBOX_TOKEN
    return render(
        request, "maps/netball.html", {"mapbox_access_token": mapbox_access_token}
    )


def softball_map(request):
    mapbox_access_token = MAPBOX_TOKEN
    return render(
        request, "maps/softball.html", {"mapbox_access_token": mapbox_access_token}
    )


def volleyball_map(request):
    mapbox_access_token = MAPBOX_TOKEN
    return render(
        request, "maps/volleyball.html", {"mapbox_access_token": mapbox_access_token}
    )


def football_map(request):
    mapbox_access_token = MAPBOX_TOKEN
    return render(
        request, "maps/football.html", {"mapbox_access_token": mapbox_access_token}
    )

from django.shortcuts import render
from config.settings import MAPBOX_TOKEN


def default_map(request):
    mapbox_access_token = MAPBOX_TOKEN
    return render(
        request, "maps/map.html", {"mapbox_access_token": mapbox_access_token}
    )

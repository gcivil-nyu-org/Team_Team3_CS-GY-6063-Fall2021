from django.shortcuts import render
from maps.facilities_data import read_facilities_data, read_hiking_data
from events.models import Event
from config.settings import MAPBOX_TOKEN

import json

# import ast


def show(request, id, address):
    data = json.loads(read_facilities_data())
    currentFacility = data[str(id)]

    if str(id) in request.session:
        address = request.session[str(id)]
    elif str(id) not in request.session:
        request.session[str(id)] = address

    sports = {
         'Bocce': currentFacility['bocce'],
         'Track': currentFacility["track_and"],
         'Frisbee': currentFacility["frisbee"],
         'Baseball': currentFacility["adult_base"],
         'Football': currentFacility["adult_foot"],
         'Softball': currentFacility["adult_soft"],
         'Basketball': currentFacility["basketball"],
         'Cricket': currentFacility["cricket"],
         'Flag Football': currentFacility["flagfootba"],
         'Handball': currentFacility["handball"],
         'Hockey': currentFacility["hockey"],
         'Kickball': currentFacility["kickball"],
         'Lacrosse': currentFacility["lacrosse"],
         # littleLeagueBaseballOne = currentFacility["ll_baseb_1"]
         # littleLeagueBaseballTwo = currentFacility["ll_baseb_2"]
         # littleLeagueSoftball = currentFacility["ll_softbal"]
         'Netball': currentFacility["netball"],
         'Rugby': currentFacility["rugby"],
         'Tennis': currentFacility["tennis"],
         'Volleyball': currentFacility["volleyball"]
    }

    name = currentFacility["name"]
    accessible = currentFacility["accessible"]
    # description = currentFacility["descriptio"]
    dimensions = currentFacility["dimensions"]
    wheelchair = currentFacility["wheelchair"]
    coordinates = currentFacility['geometry']['coordinates']

    eventsAtLocation = Event.objects.filter(locationId = id);
    return render(
        request,
        "maps/facilities.html",
        {
            "sports": sports,
            "id": id,
            "address": address,
            "currentFacility": currentFacility,
            "name": name,
            "accessible": accessible,
            "dimensions": dimensions,
            "wheelchair": wheelchair,
            "events": eventsAtLocation,
            "coordinates": coordinates,
            "mapbox_access_token": MAPBOX_TOKEN
        },
    )

def trails(request, id):
    data = json.loads(read_hiking_data())
    currentTrail = data[str(id)]

    name = currentTrail["Name"]
    location = currentTrail["Location"]
    park = currentTrail["Park_Name"]
    length = currentTrail["Length"]
    difficulty = currentTrail["Difficulty"]
    details = currentTrail["Other_Details"]
    accessible = currentTrail["Accessible"]
    limited_access = currentTrail["Limited_Access"]

    eventsAtLocation = Event.objects.filter(locationId = id)

    return render(
        request,
        "maps/trails.html",
        {
            "id": id,
            "name": name,
            "location" : location,
            "park" : park,
            "length": length,
            "difficulty": difficulty,
            "details": details,
            "accessible": accessible,
            "limited_access": limited_access,
            "events": eventsAtLocation
        },
    )

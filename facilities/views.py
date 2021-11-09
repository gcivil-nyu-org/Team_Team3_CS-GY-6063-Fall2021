from django.shortcuts import render
from maps.facilities_data import read_facilities_data, read_hiking_data
from events.models import Event
from config.settings import MAPBOX_TOKEN

import json

# import ast


def show(request, id):
    data = json.loads(read_facilities_data())
    currentFacility = data[str(id)]

    track = currentFacility["track_and"]
    name = currentFacility["name"]
    bocce = currentFacility["bocce"]
    frisbee = currentFacility["frisbee"]
    tBall = currentFacility["t_ball"]
    accessible = currentFacility["accessible"]
    adultBaseball = currentFacility["adult_base"]
    adultFootball = currentFacility["adult_foot"]
    adultSoftball = currentFacility["adult_soft"]
    basketball = currentFacility["basketball"]
    cricket = currentFacility["cricket"]
    description = currentFacility["descriptio"]
    dimensions = currentFacility["dimensions"]
    flagFootball = currentFacility["flagfootba"]
    handball = currentFacility["handball"]
    hockey = currentFacility["hockey"]
    kickball = currentFacility["kickball"]
    lacrosse = currentFacility["lacrosse"]
    littleLeagueBaseballOne = currentFacility["ll_baseb_1"]
    littleLeagueBaseballTwo = currentFacility["ll_baseb_2"]
    littleLeagueSoftball = currentFacility["ll_softbal"]
    netball = currentFacility["netball"]
    rugby = currentFacility["rugby"]
    tennis = currentFacility["tennis"]
    volleyball = currentFacility["volleyball"]
    wheelchair = currentFacility["wheelchair"]
    youthFootball = currentFacility["youth_foot"]
    coordinates = currentFacility['geometry']['coordinates']

    eventsAtLocation = Event.objects.filter(locationId = id);
    return render(
        request,
        "maps/facilities.html",
        {
            "id": id,
            "currentFacility": currentFacility,
            "track": track,
            "name": name,
            "bocce": bocce,
            "frisbee": frisbee,
            "tball": tBall,
            "accessible": accessible,
            "adultBaseball": adultBaseball,
            "adultFootball": adultFootball,
            "adultSoftball": adultSoftball,
            "description": description,
            "basketball": basketball,
            "cricket": cricket,
            "dimensions": dimensions,
            "flagFootball": flagFootball,
            "handball": handball,
            "hockey": hockey,
            "kickball": kickball,
            "lacrosse": lacrosse,
            "littleLeagueBaseBallOne": littleLeagueBaseballOne,
            "littleLeagueBaseBallTwo": littleLeagueBaseballTwo,
            "littleLeagueSoftball": littleLeagueSoftball,
            "netball": netball,
            "rugby": rugby,
            "tennis": tennis,
            "volleyball": volleyball,
            "wheelchair": wheelchair,
            "youthFootball": youthFootball,
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

from django.http import HttpResponse
from maps.facilities_data import read_facilities_data
import json

def show(request, id):
    data = json.loads(read_facilities_data());
    currentFacility = data[str(id)];

    return HttpResponse(f'<div> this will be the page for the facility with mapbox objectid: { id } </div> <div>{currentFacility}</div>')

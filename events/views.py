from django.shortcuts import render
from maps.facilities_data import read_facilities_data
import json
# import ast


def add_event(request):
    return render(
        request,
        "events/add_event.html",
    )

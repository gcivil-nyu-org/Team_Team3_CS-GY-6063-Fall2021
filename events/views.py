from django.shortcuts import render
from .models import Event

# Create your views here.
def event(request):
  context = {
    'event': Event.objects.all().last()
  }

  return render(request, "events/event.html", context)

def add_event(request, id):
  return render(request, "events/add_event.html", {"id": id})

from django.conf.urls import url
from django.urls import path
from .views import EventsListView, EventsCreateView, EventDetailView
from . import views

urlpatterns = [
  path('', EventsListView.as_view(), name='events-list'),
  path('event/<pk>/', EventDetailView.as_view(), name='events-detail'),
  path("event/new/<id>", EventsCreateView.as_view(), name="add-event"),
]

from django.conf.urls import url
from django.urls import path
from .views import EventsListView, EventsCreateView, EventDetailView, EventUpdateView
from . import views

urlpatterns = [
  path('', EventsListView.as_view(), name='events-list'),
  path('<pk>/', EventDetailView.as_view(), name='event-detail'),
  path('<pk>/update/', EventUpdateView.as_view(), name='event-update'),
  path("new/<id>/", EventsCreateView.as_view(), name="add-event"),
]

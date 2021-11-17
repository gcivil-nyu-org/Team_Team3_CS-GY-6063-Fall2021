from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import EventsListView, EventsCreateView, EventDetailView, EventUpdateView, EventDeleteView, event_add_attendance, event_cancel_attendance

urlpatterns = [
  path("", login_required(EventsListView.as_view()), name="events-list"),
  path("<pk>/", login_required(EventDetailView.as_view()), name="event-detail"),
  path("<pk>/join/", event_add_attendance, name="join-event"),
  path("<pk>/unjoin/", event_cancel_attendance, name="unjoin-event"),
  path(
        "<pk>/update/", login_required(EventUpdateView.as_view()), name="event-update"
    ),
  path(
        "<pk>/delete/", login_required(EventDeleteView.as_view()), name="event-delete"
    ),
  path("new/<sport>/<id>/", login_required(EventsCreateView.as_view()), name="add-event"),
]

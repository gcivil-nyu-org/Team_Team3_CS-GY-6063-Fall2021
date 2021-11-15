from django.urls import path
from .views import EventsListView, EventsCreateView, EventDetailView, EventUpdateView, EventDeleteView, event_add_attendance, event_cancel_attendance

urlpatterns = [
  path('', EventsListView.as_view(), name='events-list'),
  path('<pk>/', EventDetailView.as_view(), name='event-detail'),
  path("<pk>/join/", event_add_attendance, name="join-event"),
  path("<pk>/unjoin/", event_cancel_attendance, name="unjoin-event"),
  path('<pk>/update/', EventUpdateView.as_view(), name='event-update'),
  path('<pk>/delete/', EventDeleteView.as_view(), name='event-delete'),
  path("new/<sport>/<id>/", EventsCreateView.as_view(), name="add-event"),
]

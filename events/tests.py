from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.utils import timezone
from events.models import Event
from django.urls import reverse
import datetime
from events.views import event_add_attendance, event_cancel_attendance


class EventsViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username="test_login")
        self.user.set_password("secret_111")
        self.user.save()
        time = timezone.now() + datetime.timedelta(days=30)
        Event.objects.create(
            name="test event",
            description="description",
            address="123 abc st",
            locationId="12",
            date=time,
            dateCreated=time,
            owner=self.user,
        )

    def test_events_list_view(self):
        response = self.client.get("/events/")
        self.assertEqual(response.status_code, 302)

    def test_events_detail_view(self):
        c = Client()
        c.login(username="test_login", password="secret_111")
        response = c.get(reverse("event-detail", kwargs={"pk": 1}))
        self.assertEqual(response.status_code, 200)

    def test_create_event(self):
        c = Client()
        c.login(username="test_login", password="secret_111")
        response = c.get(reverse("add-event", kwargs={"id": 1}))
        self.assertEqual(response.status_code, 200)

    def test_update_event(self):
        c = Client()
        c.login(username="test_login", password="secret_111")
        response = c.get(reverse("event-update", kwargs={"pk": 1}))
        self.assertEqual(response.status_code, 200)

    def test_get_registration(self):
        time = timezone.now() + datetime.timedelta(days=30)
        event = Event.objects.create(
            name="test event",
            description="description",
            address="123 abc st",
            locationId="12",
            date=time,
            dateCreated=time,
            owner=self.user,
        )
        test = event.get_registrations()
        self.assertEqual(test.count(), 0)

    def test_get_absolute_url(self):
        time = timezone.now() + datetime.timedelta(days=30)
        event = Event.objects.create(
            name="test event",
            description="description",
            address="123 abc st",
            locationId="12",
            date=time,
            dateCreated=time,
            owner=self.user,
        )
        url = event.get_absolute_url()
        self.assertEqual(url, "/events/2/")

    def test_add_user_to_list_of_attendees(self):
        time = timezone.now() + datetime.timedelta(days=30)
        event = Event.objects.create(
            name="test event",
            description="description",
            address="123 abc st",
            locationId="12",
            date=time,
            dateCreated=time,
            owner=self.user,
        )
        registration = event.add_user_to_list_of_attendees(self.user)
        self.assertEqual(type(registration).__name__, "EventRegistration")

    def test_remove_user_from_list_of_attendees(self):
        time = timezone.now() + datetime.timedelta(days=30)
        event = Event.objects.create(
            name="test event",
            description="description",
            address="123 abc st",
            locationId="12",
            date=time,
            dateCreated=time,
            owner=self.user,
        )
        event.add_user_to_list_of_attendees(self.user)
        removeRegistration = event.remove_user_from_list_of_attendees(self.user)
        self.assertEqual(removeRegistration, True)

    def test_event_add_and_cancel_attendance(self):
        c = Client()
        c.login(username="test_login", password="secret_111")
        response = c.get(reverse("event-detail", kwargs={"pk": 1}))
        self.assertEqual(response.status_code, 200)
        response.user = self.user
        event_add_attendance(response, 1)
        event_cancel_attendance(response, 1)
        self.assertTemplateUsed(response, "events/events_detail.html")

    def test_create_event_view(self):
        c = Client()
        c.login(username="test_login", password="secret_111")
        response = c.get(reverse("add-event", kwargs={"id": 15385}))
        self.assertEqual(response.status_code, 200)

from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.utils import timezone
from events.models import Event
from django.urls import reverse
import datetime
from events.views import event_add_attendance, event_cancel_attendance, get_sport_key

class EventsViewTest(TestCase):

  def setUp(self):
    self.user = User.objects.create(username = 'test_login')
    self.user.set_password('secret_111')
    self.user.save()
    time = timezone.now() + datetime.timedelta(days=30)
    Event.objects.create(name="test event", description="description", address="123 abc st", locationId="12", date=time, dateCreated=time, owner=self.user, numberOfPlayers=5)

  def test_events_list_view(self):
    c = Client()
    c.login(username = 'test_login', password = 'secret_111')
    response = c.get('/events/')
    self.assertEqual(response.status_code, 200)

  def test_events_detail_view(self):
    c = Client()
    c.login(username = 'test_login', password = 'secret_111')
    time = timezone.now()
    event =  Event.objects.create(name="test event", description="description", address="123 abc st", locationId="12", date=time, dateCreated=time, owner=self.user, numberOfPlayers=5)
    event.add_user_to_list_of_attendees(self.user)
    pk = event.pk
    response = c.get(reverse('event-detail', kwargs={'pk':pk}))
    self.assertEqual(response.status_code, 200)

  def test_create_event(self):
    c = Client()
    c.login(username = 'test_login', password = 'secret_111')
    response = c.get(reverse('add-event', kwargs={'id':1, 'sport': 'baseball'}))
    self.assertEqual(response.status_code, 200)

  def test_update_event(self):
    c = Client()
    c.login(username = 'test_login', password = 'secret_111')
    response = c.get(reverse('event-update', kwargs={'pk':1}))
    self.assertEqual(response.status_code, 200)

  def test_get_registration(self):
    time = timezone.now() + datetime.timedelta(days=30)
    event =  Event.objects.create(name="test event", description="description", address="123 abc st", locationId="12", date=time, dateCreated=time, owner=self.user, numberOfPlayers=5)
    test = event.get_registrations()
    self.assertEqual(test.count(), 0)

  def test_get_absolute_url(self):
    time = timezone.now() + datetime.timedelta(days=30)
    event =  Event.objects.create(name="test event", description="description", address="123 abc st", locationId="12", date=time, dateCreated=time, owner=self.user, numberOfPlayers=5)
    url = event.get_absolute_url()
    self.assertEqual(url, '/events/2/')

  def test_add_user_to_list_of_attendees(self):
    time = timezone.now() + datetime.timedelta(days=30)
    event =  Event.objects.create(name="test event", description="description", address="123 abc st", locationId="12", date=time, dateCreated=time, owner=self.user, numberOfPlayers=2)
    user2 = User.objects.create(username = 'test_login2')
    registration = event.add_user_to_list_of_attendees(user2)
    c = Client()
    c.login(username = 'test_login', password = 'secret_111')
    c.post(reverse('join-event', kwargs={'pk':event.pk}))
    test = event.get_registrations()
    self.assertEqual(type(registration).__name__, 'EventRegistration')
    self.assertEqual(test.count(), 2)

  def test_remove_user_from_full_list_of_attendees(self):
    time = timezone.now() + datetime.timedelta(days=30)
    user2 = User.objects.create(username = 'test_login2')
    event =  Event.objects.create(name="test event", description="description", address="123 abc st", locationId="12", date=time, dateCreated=time, owner=self.user, numberOfPlayers=2)
    event.add_user_to_list_of_attendees(self.user)
    event.add_user_to_list_of_attendees(user2)
    c = Client()
    c.login(username = 'test_login', password = 'secret_111')
    c.post(reverse('unjoin-event', kwargs={'pk':event.pk}))
    test = event.get_registrations()
    self.assertEqual(test.count(), 1)

  def test_event_add_and_cancel_attendance(self):
    c = Client()
    c.login(username = 'test_login', password = 'secret_111')
    response = c.get(reverse('event-detail', kwargs={'pk':1}))
    self.assertEqual(response.status_code, 200)
    response.user = self.user
    event_add_attendance(response, 1)
    event_cancel_attendance(response, 1)
    self.assertTemplateUsed(response, "events/events_detail.html")

  def test_create_event_view(self):
    c = Client()
    c.login(username = 'test_login', password = 'secret_111')
    response = c.get(reverse('add-event', kwargs={'id':15385, 'sport': 'baseball'}))
    self.assertEqual(response.status_code, 200)

  def test_get_sport_key(self):
    key = get_sport_key('Baseball');
    self.assertEqual(key, 'adult_base')

  def test_join_full_event(self):
    time = timezone.now() + datetime.timedelta(days=30)
    event =  Event.objects.create(name="testevent", description="description", address="123 abc st", locationId="12", date=time, dateCreated=time, owner=self.user, numberOfPlayers=2)
    user2 = User.objects.create(username = 'test_login2')
    user3 = User.objects.create(username = 'test_login3')
    event.add_user_to_list_of_attendees(user3)
    event.add_user_to_list_of_attendees(user2)
    c = Client()
    c.login(username = 'test_login', password = 'secret_111')
    c.post(reverse('join-event', kwargs={'pk':event.pk}))
    test = event.get_registrations()
    self.assertEqual(test.count(), 2)

  def test_leave_full_event(self):
    time = timezone.now() + datetime.timedelta(days=30)
    event =  Event.objects.create(name="test event", description="description", address="123 abc st", locationId="12", date=time, dateCreated=time, owner=self.user, numberOfPlayers=2)
    user2 = User.objects.create(username = 'test_login2')
    event.add_user_to_list_of_attendees(self.user)
    event.add_user_to_list_of_attendees(user2)
    event.remove_user_from_list_of_attendees(self.user)
    test = event.get_registrations()
    self.assertEqual(test.count(), 1)
  
  def test_delete_event(self):
    c = Client()
    c.login(username = 'test_login', password = 'secret_111')
    time = timezone.now()
    event =  Event.objects.create(name="test event", description="description", address="123 abc st", locationId="12", date=time, dateCreated=time, owner=self.user, numberOfPlayers=5)
    response = c.post(reverse('event-delete', kwargs={'pk':event.pk}))
    self.assertTrue(response)

class SquadTest(TestCase):
  def test_squad(self):
    time = timezone.now() + datetime.timedelta(days=30)
    self.user = User.objects.create(username = 'test_login')
    self.user.set_password('secret_111')
    self.user.save()
    event = Event.objects.create(name="test event", description="description", address="123 abc st", locationId="12", date=time, dateCreated=time, owner=self.user, numberOfPlayers=5)
    self.user2 = User.objects.create(username = 'test_login_2')
    self.user2.set_password('secret_1112')
    self.user2.save()
    c = Client()
    c.login(username = 'test_login', password = 'secret_111')
    event.add_user_to_list_of_attendees(self.user)
    event.add_user_to_list_of_attendees(self.user2)
    response = c.get("/squad")
    self.assertEqual(response.status_code, 200)
    self.assertContains(response, "test_login_2")

from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.utils import timezone
from events.models import Event
from django.urls import reverse
import datetime

class EventsViewTest(TestCase):

  def setUp(self):
    self.user = User.objects.create(username = 'test_login')
    self.user.set_password('secret_111')
    self.user.save()
    time = timezone.now() + datetime.timedelta(days=30)
    Event.objects.create(name="test event", description="description", address="123 abc st", locationId="12", date=time, dateCreated=time, owner=self.user)

  def test_events_list_view(self):
    response = self.client.get('/events/')
    self.assertEqual(response.status_code, 200)
    self.assertTemplateUsed(response, 'events/events_list.html')
  
  def test_events_detail_view(self):
    c = Client()
    c.login(username = 'test_login', password = 'secret_111')
    response = c.get(reverse('event-detail', kwargs={'pk':1}))
    self.assertEqual(response.status_code, 200)

  def test_create_event(self):
    c = Client()
    c.login(username = 'test_login', password = 'secret_111')
    response = c.get(reverse('add-event', kwargs={'id':1}))
    self.assertEqual(response.status_code, 200)

  def test_update_event(self):
    c = Client()
    c.login(username = 'test_login', password = 'secret_111')
    response = c.get(reverse('event-update', kwargs={'pk':1}))
    self.assertEqual(response.status_code, 200)

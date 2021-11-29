from django.test import TestCase, Client
from django.contrib.auth.models import User
from .models import Noshow, Misbehavior


class TestReportingViews(TestCase):
    def setUp(self):
        self.user = User.objects.create(username = 'test_login')
        self.user.set_password('secret_111')
        self.user.save()

    def test_ContactUs_view(self):
        response = self.client.get('reporting/contactus.html')
        self.assertEqual(response.status_code, 404)

    def test_reporting_no_show_success(self):
        c = Client()
        c.login(username = 'test_login', password = 'secret_111')
        self.user2 = User.objects.create(username = 'test_login_2')
        c.post('/reporting/report_noshow', {'name': self.user2.id, 'description': 'description'})
        self.assertEqual(Noshow.objects.filter(name=self.user2).exists(), True)

    def test_reporting_misbehavior_success(self):
        c = Client()
        c.login(username = 'test_login', password = 'secret_111')
        self.user2 = User.objects.create(username = 'test_login_2')
        c.post('/reporting/report_misbehavior', {'name': self.user2.id, 'description': 'description'})
        self.assertEqual(Misbehavior.objects.filter(name=self.user2).exists(), True)

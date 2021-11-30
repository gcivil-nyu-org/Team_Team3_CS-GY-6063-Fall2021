from django.test import TestCase, Client
from django.contrib.auth.models import User
from .models import Noshow, Misbehavior
from reporting.forms import ReportNoShowForm, ReportMisbehaviorForm


class TestReportingViews(TestCase):
    def setUp(self):
        self.user = User.objects.create(username = 'test_login')
        self.user.set_password('secret_111')
        self.user.save()

    def test_ContactUs_view(self):
        response = self.client.get('reporting/contactus.html')
        self.assertEqual(response.status_code, 404)

    def test_ContactUs_view_logged_in(self):
        c = Client()
        c.login(username = 'test_login', password = 'secret_111')
        response = c.get('/reporting/contact_us')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "reporting/contactus.html")

    def test_reporting_no_show(self):
        c = Client()
        c.login(username = 'test_login', password = 'secret_111')
        response = c.get('/reporting/report_noshow')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "reporting/noshow.html")
        self.assertIsInstance(response.context['form'], ReportNoShowForm)

    def test_reporting_no_show_success(self):
        c = Client()
        c.login(username = 'test_login', password = 'secret_111')
        self.user2 = User.objects.create(username = 'test_login_2')
        c.post('/reporting/report_noshow', {'name': self.user2.id, 'description': 'description'})
        self.assertEqual(Noshow.objects.filter(name=self.user2).exists(), True)

    def test_reporting_misbehavior(self):
        c = Client()
        c.login(username = 'test_login', password = 'secret_111')
        response = c.get('/reporting/report_misbehavior')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "reporting/misbehavior.html")
        self.assertIsInstance(response.context['form'], ReportMisbehaviorForm)

    def test_reporting_misbehavior_success(self):
        c = Client()
        c.login(username = 'test_login', password = 'secret_111')
        self.user2 = User.objects.create(username = 'test_login_2')
        c.post('/reporting/report_misbehavior', {'name': self.user2.id, 'description': 'description'})
        self.assertEqual(Misbehavior.objects.filter(name=self.user2).exists(), True)

from django.test import TestCase
from django.contrib.auth.models import User


class TestReportingViews(TestCase):
    def setUp(self):
        self.user = User.objects.create(username = 'test_login')
        self.user.set_password('secret_111')
        self.user.save()

    def test_ContactUs_view(self):
        response = self.client.get('reporting/contactus.html')
        self.assertEqual(response.status_code, 404)
       
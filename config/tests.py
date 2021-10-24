from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.auth import authenticate



class TestUserLogin(TestCase):

    def setUp(self):
        self.user = User.objects.create(username='test_login')
        self.user.set_password('secret_111')
        self.user.save()

    def test_login_get_page(self):
        c = Client()
        response = c.get(reverse('login'))
        self.assertEqual(response.status_code, 200)

    def test_login_success(self):
        c = Client()
        status = c.login(username = 'test_login', password = 'secret_111')
        self.assertTrue(status)

    def test_login_failure(self):
        c = Client()
        status = c.login(username = 'test_login', password = 'incorrectpassword')
        self.assertFalse(status)

    def test_unknown_username(self):
        user = authenticate(username = 'not_a_valid_username_222', password = 'incorrectpassword')
        self.assertIsNone(user)
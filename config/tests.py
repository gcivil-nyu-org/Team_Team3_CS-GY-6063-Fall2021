from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.auth import authenticate


# A LOGGED IN USER IS STILL ABLE TO ACCESS THE LOGIN PAGE MANUALLY
# INCLUDE TEST FOR THIS AFTER UPDATING CODE

class TestUserLogin(TestCase):

    def setUp(self):
        self.user = User.objects.create(username='test_login')
        self.user.set_password('secret_111')
        self.user.save()

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

    #Idea: Log Out is only in the dropdown. Tets that only a logged in user can see this string in the dropdown
    def test_logged_in_user_sees_dashboard_dropdown(self):
        c = Client()
        status = c.login(username = 'test_login', password = 'secret_111')
        response = c.get(reverse('login'))
        self.assertContains(response, 'Log Out')

    #Idea: Tets that a logged out user cannot see the dropdown, because response does not contain Log Out
    def logged_out_user_can_log_in(self):
        c = Client()
        status = c.logout()
        response = c.get(reverse('logout'))
        self.assertNotContains(response, 'Log Out')

class TestUserLoginViews(TestCase):

        def test_view_url_exists_in_expected_location(self):
            response = self.client.get('/accounts/login/')
            self.assertEqual(response.status_code, 200)

        def test_view_url_accessible_by_name(self):
            c = Client()
            response = c.get(reverse('login'))
            self.assertEqual(response.status_code, 200)

        def test_view_uses_correct_template(self):
            c = Client()
            response = c.get(reverse('login'))
            self.assertEqual(response.status_code, 200)
            self.assertTemplateUsed(response, 'registration/login.html')

from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.test.client import RequestFactory
from django.urls import reverse
from django.contrib.auth import authenticate
from .views import HomePageView

# A LOGGED IN USER IS STILL ABLE TO ACCESS THE LOGIN PAGE MANUALLY
# INCLUDE TEST FOR THIS AFTER UPDATING CODE


class TestUserLogin(TestCase):

    @classmethod
    def setUpTestData(cls):
        super().setUpTestData()
        cls.user = User.objects.create(username="test_login")
        cls.user.set_password("secret_111")
        cls.user.save()
        cls.c = Client()

    def test_login_success(self):
        status = self.c.login(username="test_login", password="secret_111")
        self.assertTrue(status)

    def test_login_failure(self):
        status = self.c.login(username="test_login", password="incorrectpassword")
        self.assertFalse(status)

    def test_unknown_username(self):
        user = authenticate(
            username="not_a_valid_username_222", password="incorrectpassword"
        )
        self.assertIsNone(user)

    # Idea: Log Out is only in the dropdown.
    #Only a logged in user can see this string in the dropdown
    def test_logged_in_user_sees_dashboard_dropdown(self):
        self.c.login(username="test_login", password="secret_111")
        response = self.c.get(reverse("login"))
        self.assertContains(response, "Log Out")

    # Idea: Tets that a logged out user cannot see the dropdown
    #because response does not contain Log Out
    def  logged_out_user_can_log_in(self):
        self.c.logout()
        response = self.c.get(reverse("logout"))
        self.assertNotContains(response, "Log Out")


class TestUserLoginViews(TestCase):
    @classmethod
    def setUpTestData(cls):
        super().setUpTestData()
        cls.c = Client()

    def test_view_url_exists_in_expected_location(self):
        response = self.client.get("/accounts/login/")
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.c.get(reverse("login"))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.c.get(reverse("login"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "registration/login.html")

class TestHomePageView(TestCase, RequestFactory):
    def setUp(self):
        # Every test needs access to the request factory.
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            username="test_login", password="secret_111", email= "testemail@gmail.com")

    def test_context(self):
        request = self.factory.get('/')
        request.user = self.user
        response = HomePageView.as_view(template_name="home.html")(request)
        self.assertIsInstance(response.context_data, dict)

class TestAboutPage(TestCase):
    def test_about_view_url(self):
        response = self.client.get("/about")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "About Us")

from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from .tokens import account_activation_token


class BaseTest(TestCase):
    def setUp(self):
        self.signup_url = reverse("signup")
        self.user = {
            "username": "testuser",
            "email": "testemail@gmail.com",
            "first_name": "test",
            "last_name": "user",
            "password1": "OutdoorSquad",
            "password2": "OutdoorSquad",
        }
        return super().setUp()


class RegistrationTest(BaseTest):
    def test_can_view_signup_page_correctly(self):
        response = self.client.get(self.signup_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "signup.html")

    def test_can_register_user(self):
        response = self.client.post(self.signup_url, self.user)
        self.assertRedirects(response, '/', status_code=302, target_status_code=200)


class UserActivationTest(TestCase):
    def test_user_activate_success(self):
        user = User.objects.create_user("testuser1")
        user.set_password("OutdoorSquad")
        uid = urlsafe_base64_encode(force_bytes(user.pk))
        token = account_activation_token.make_token(user)
        response = self.client.get(
            reverse("activate", kwargs={"uidb64": uid, "token": token})
        )
        self.assertEqual(response.status_code, 302)
        user = User.objects.get(username="testuser1")
        self.assertTrue(user.is_active)

    def test_user_activate_fail(self):
        user = User.objects.create_user("testuser2")
        user.set_password("OutdoorSquad")
        token = account_activation_token.make_token(user)
        with self.assertRaises(User.DoesNotExist):
            response = self.client.get(
                reverse("activate", kwargs={"uidb64": "123", "token": token})
            )
            self.assertEqual(response.status_code, 302)
            user = User.objects.get(username="testuser3")

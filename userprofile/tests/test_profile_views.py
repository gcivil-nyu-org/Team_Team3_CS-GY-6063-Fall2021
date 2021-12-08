from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse


class TestUserProfileViews(TestCase):

    @classmethod
    def setUpTestData(cls):
        super().setUpTestData()
        cls.user = User.objects.create(username="test_login")
        cls.user.set_password("secret_111")
        cls.user.save()

    def test_view_userprofile_access_requires_login(self):
        c = Client()
        response = c.get("/userprofile/edit_profile/")
        self.assertEqual(response.status_code, 302)

        response = c.get("/userprofile/profile_page/")
        self.assertEqual(response.status_code, 302)

    def test_view_userprofile_exists_in_expected_location(self):
        c = Client()
        c.login(username="test_login", password="secret_111")
        response = c.get("/userprofile/edit_profile/")
        self.assertEqual(response.status_code, 200)

        response = c.get("/userprofile/profile/")
        self.assertEqual(response.status_code, 200)

    def test_view_userprofile_accessible_by_name(self):
        c = Client()
        c.login(username="test_login", password="secret_111")
        response = c.get(reverse("profile_edit"))
        self.assertEqual(response.status_code, 200)

        response = c.get(reverse("profile_page"))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        c = Client()
        c.login(username="test_login", password="secret_111")
        response = c.get(reverse("profile_edit"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "userprofile/edit_profile.html")

        response = c.get(reverse("profile_page"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "userprofile/profile_page.html")

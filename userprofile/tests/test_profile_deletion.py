from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from userprofile.models import Profile
from userprofile.views import delete_profile


class TestUserProfileCreation(TestCase):

    @classmethod
    def setUpTestData(cls):
        super().setUpTestData()
        cls.user = User.objects.create(username="testuser")
        cls.user.set_password("secret_111")
        cls.user.save()
        cls.c = Client()
        cls.c.login(username="testuser", password="secret_111")

    def test_delete_existing_user(self):
        #check that the user and their profile exists
        user = User.objects.get(username="testuser")
        Profile.objects.get(user=user.pk)

        response = self.c.post('userprofile/delete_profile')
        request = response.wsgi_request
        delete_profile(request)

        with self.assertRaises(User.DoesNotExist):
            user = User.objects.get(username="testuser")
        with self.assertRaises(Profile.DoesNotExist):   
            Profile.objects.get(user=user.pk)

    def test_get_template_no_deletion(self):

        user = User.objects.get(username="testuser")
        profile = Profile.objects.get(user=user.pk)

        response = self.c.get("/userprofile/delete_profile/")
        request = response.wsgi_request
        delete_profile(request)

        self.assertEqual(user, User.objects.get(username="testuser"))
        self.assertEqual(profile, Profile.objects.get(user=user.pk))

    def test_template_accessible_by_name(self):

        response = self.c.get(reverse("profile_delete"))
        self.assertEqual(response.status_code, 200)
    
    def test_uses_correct_template(self):
        
        response = self.c.get(reverse("profile_delete"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "userprofile/delete_profile.html")
        
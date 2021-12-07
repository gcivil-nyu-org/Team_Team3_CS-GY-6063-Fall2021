from django.test import TestCase
from django.contrib.auth.models import User
from userprofile.forms import ProfileUpdateForm

class TestUserProfileCreation(TestCase):
    
    @classmethod
    def setUpTestData(cls):
        super().setUpTestData()
        cls.user = User.objects.create(username="test_login")
        cls.user.set_password("secret_111")
        cls.user.save()

    def test_form_valid(self):
        form_data = {
            "profilename": "testuser12",
            "tennis": True,
            "frisbee": False,
            "hiking": True,
            "location": "nyc",
            "distance": 1,
        }
        form = ProfileUpdateForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_form_invalid_text(self):
        form_data = {
            "profilename": "testuser12",
            "tennis": "true",
            "frisbee": False,
            "hiking": True,
            "location": "nyc",
            "distance": "one mile",
        }
        form = ProfileUpdateForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_create_profile_saves_correct_data(self):

        self.client.login(username="test_login", password="secret_111")
        form_data = {
            "profilename": "testuser12",
            "tennis": True,
            "frisbee": False,
            "hiking": True,
            "location": "nyc",
            "distance": 1,
        }
        response = self.client.post("/userprofile/edit_profile/", form_data)
        self.assertContains(response, "testuser12")

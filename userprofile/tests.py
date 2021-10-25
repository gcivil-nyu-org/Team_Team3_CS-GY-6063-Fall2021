from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse


class TestUserLoginViews(TestCase):

    def setUp(self):
        self.user = User.objects.create(username='test_login')
        self.user.set_password('secret_111')
        self.user.save()
    
    def test_view_userprofile_access_requires_login(self):
        c = Client()
        response = c.get('/userprofile/')
        self.assertEqual(response.status_code, 302)

    def test_view_userprofile_exists_in_expected_location(self):
        c = Client()
        c.login(username = 'test_login', password = 'secret_111')
        response = c.get('/userprofile/')
        self.assertEqual(response.status_code, 200)

    def test_view_userprofile_accessible_by_name(self):
        c = Client()
        c.login(username = 'test_login', password = 'secret_111')
        response = c.get(reverse('user-profile'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        c = Client()
        c.login(username = 'test_login', password = 'secret_111')
        response = c.get(reverse('user-profile'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'userprofile/profile.html')
    
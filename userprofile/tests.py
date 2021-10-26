from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse


class TestUserProfileViews(TestCase):

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

from .forms import ProfileUpdateForm
from .models import Profile

class TestUserProfileCreation(TestCase):

    def setUp(self):
        self.user = User.objects.create(username='test_login')
        self.user.set_password('secret_111')
        self.user.save()
        
        # self.client.login(username = 'test_login', password = 'secret_111')
        #self.client.get('/userprofile/')


    def test_form_valid(self):
        form_data = {
            'profilename':'testuser12',
            'tennis':True,
            'frisbee':False,
            'hiking':True,
            'location':'nyc',
            'distance':1,
        } 
        form = ProfileUpdateForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_form_invalid_text(self):
        form_data = {
            'profilename':'testuser12',
            'tennis':'true',
            'frisbee':False,
            'hiking':True,
            'location':'nyc',
            'distance':'one mile',
        }
        form = ProfileUpdateForm(data=form_data)
        self.assertFalse(form.is_valid())
    
    def test_create_profile_saves_correct_data(self):
        
        self.client.login(username = 'test_login', password = 'secret_111')
        form_data = {
            'profilename':'testuser12',
            'tennis':True,
            'frisbee':False,
            'hiking':True,
            'location':'nyc',
            'distance':1,
        } 
        response = self.client.post('/userprofile/', form_data)
        self.assertContains(response, 'testuser12')
        #self.assertTrue(Profile.objects.filter(profilename='testuser12').exists())

#NEED TESTS FOR WHEN A USER UPDATES THEIR PROFILE
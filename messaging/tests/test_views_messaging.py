from django.test import TestCase, Client
from django.contrib.auth.models import User
from messaging.models import ThreadModel, MessageModel
from django.urls import reverse

class CreateThreadViewsTests(TestCase):

    def setUp(self):
        self.user1 = User.objects.create(username = 'sender')
        self.user2 = User.objects.create(username = 'receiver')
        self.user1.set_password("secret_111")
        self.user2.set_password("secret_111")
        self.user1.save()
        self.user2.save()
        self.c = Client()
        
    def test_create_thread_view_accessible(self):
        self.c.login(username="sender", password="secret_111")
        response = self.c.get(reverse("create-thread"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "messaging/create_thread.html")

    def test_post_blank_form(self):
        self.c.login(username="sender", password="secret_111")
        response = self.c.post(reverse("create-thread"), {})
        self.assertRedirects(response, "/messaging/inbox/create-thread", status_code=302)
    
    def test_thread_exists_and_sender_created(self):
        self.c.login(username="sender", password="secret_111")
        thread = ThreadModel.objects.create(user = self.user1, receiver = self.user2)
        MessageModel(thread=thread, sender_user=self.user1, receiver_user=self.user2, body='test') 
        response = self.c.post(reverse("create-thread"), {'username':'receiver'})
        self.assertRedirects(response, "/messaging/inbox/"+str(thread.pk)+'/', status_code=302)

    def test_thread_exists_and_receiver_created(self):
        self.c.login(username="sender", password="secret_111")
        thread = ThreadModel.objects.create(user = self.user2, receiver = self.user1)
        MessageModel(thread=thread, sender_user=self.user2, receiver_user=self.user1, body='test') 
        response = self.c.post(reverse("create-thread"), {'username':'receiver'})
        self.assertRedirects(response, "/messaging/inbox/"+str(thread.pk)+'/', status_code=302)

    def test_thread_does_not_exist(self):
        self.c.login(username="sender", password="secret_111")
        response = self.c.post(reverse("create-thread"), {'username':'receiver'})
        self.assertEqual(response.status_code, 302)

class ListThreadViewsTests(TestCase):

    def setUp(self):
        self.user1 = User.objects.create(username = 'sender')
        self.user1.set_password("secret_111")
        self.user1.save()
        self.c = Client()
    
    def test_inbox_view_accessible(self):
        self.c.login(username="sender", password="secret_111")
        response = self.c.get(reverse("inbox"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "messaging/inbox.html")

class CreateMessageViewsTests(TestCase):
    def setUp(self):
        self.user1 = User.objects.create(username = 'sender')
        self.user2 = User.objects.create(username = 'receiver')
        self.user1.set_password("secret_111")
        self.user1.save()
        self.c = Client()

    def test_send_message_to_senders_thread(self):
        self.c.login(username="sender", password="secret_111")
        thread = ThreadModel.objects.create(user = self.user1, receiver = self.user2)
        pk = thread.pk
        response = self.c.post("/messaging/inbox/"+str(pk)+"/create-message/", {'message':'hello this is a test message'})
        self.assertRedirects(response, '/messaging/inbox/'+str(pk)+'/', status_code=302)

    def test_send_message_to_receivers_thread(self):
        self.c.login(username="sender", password="secret_111")
        thread = ThreadModel.objects.create(user = self.user2, receiver = self.user1)
        pk = thread.pk
        response = self.c.post("/messaging/inbox/"+str(pk)+"/create-message/", {'message':'hello this is a test message'})
        self.assertRedirects(response, '/messaging/inbox/'+str(pk)+'/', status_code=302) 

class CreateMessageViewsTests(TestCase):
    def setUp(self):
        self.user1 = User.objects.create(username = 'sender')
        self.user2 = User.objects.create(username = 'receiver')
        self.user1.set_password("secret_111")
        self.user1.save()
        self.c = Client()
        self.thread = ThreadModel.objects.create(user = self.user1, receiver = self.user2)

    def test_thread_view_accessible(self):
        self.c.login(username="sender", password="secret_111")
        pk = self.thread.pk
        response = self.c.get("/messaging/inbox/"+str(pk)+"/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "messaging/thread.html")

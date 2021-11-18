from django.test import TestCase
from django.contrib.auth.models import User
from messaging.models import ThreadModel, MessageModel

class ThreadModelTest(TestCase):

    def setUp(self):
        self.user1 = User.objects.create(username = 'sender')
        self.user2 = User.objects.create(username = 'receiver')
        ThreadModel.objects.create(user = self.user1, receiver = self.user2)

    def test_thread_model_defaults(self):
        thread = ThreadModel.objects.get(user = self.user1, receiver = self.user2)
        self.assertFalse(thread.has_unread)

class MessageModelTest(TestCase):

    def setUp(self):
        self.user1 = User.objects.create(username = 'sender')
        self.user2 = User.objects.create(username = 'receiver')
        ThreadModel.objects.create(user = self.user1, receiver = self.user2)
        self.thread = ThreadModel.objects.get(user = self.user1, receiver = self.user2)

    def test_check_default_values(self):
        message = "test"
        conversation = MessageModel(thread=self.thread, sender_user=self.user1, receiver_user=self.user2, body=message)  
        self.assertFalse(conversation.is_read)

        max_message_length = conversation._meta.get_field('body').max_length
        self.assertEqual(max_message_length, 1000)

from django.test import TestCase


class AddEventViewTest(TestCase):
    def test_returns_success(self):
        response = self.client.get("events/add_event/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "events/add_event.html")

from django.test import TestCase
from config.settings import MAPBOX_TOKEN

class MapsViewTest(TestCase):
    def test_returns_success(self):
        response = self.client.get('/maps/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'maps/map.html')
        self.assertContains(response, MAPBOX_TOKEN)

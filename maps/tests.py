from django.test import TestCase
from config.settings import MAPBOX_TOKEN
import json
from maps.facilities_data import read_facilities_data


class MapsViewTest(TestCase):
    def test_returns_success(self):
        response = self.client.get("/maps/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "maps/map.html")
        self.assertContains(response, MAPBOX_TOKEN)


class FacilitiesViewTest(TestCase):
    def test_returns_success(self):
        response = self.client.get("/facilities/17308")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "maps/facilities.html")


class MapsFacilitiesDataTest(TestCase):
    # test idea: checking if particular key (objectid) with a particular name is in parsed json file
    def test_returns_success(self):
        answer_dic = json.loads(read_facilities_data())
        answer_name = "Oakland Lake"
        self.assertEqual(answer_dic["13263"]["name"], answer_name)

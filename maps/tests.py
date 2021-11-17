from django.test import TestCase
from config.settings import MAPBOX_TOKEN
import json
from maps.facilities_data import read_facilities_data


class MapsViewTest(TestCase):
    def test_returns_success(self):
        response = self.client.get("/maps/map")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "maps/map.html")
        self.assertContains(response, MAPBOX_TOKEN)


class BaseballViewTest(TestCase):
    def test_returns_success(self):
        response = self.client.get("/maps/baseball")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "maps/activity.html")
        self.assertContains(response, MAPBOX_TOKEN)


class BasketballViewTest(TestCase):
    def test_returns_success(self):
        response = self.client.get("/maps/basketball")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "maps/activity.html")
        self.assertContains(response, MAPBOX_TOKEN)


class BocceViewTest(TestCase):
    def test_returns_success(self):
        response = self.client.get("/maps/bocce")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "maps/activity.html")
        self.assertContains(response, MAPBOX_TOKEN)


class CricketViewTest(TestCase):
    def test_returns_success(self):
        response = self.client.get("/maps/cricket")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "maps/activity.html")
        self.assertContains(response, MAPBOX_TOKEN)


class FlagFootballViewTest(TestCase):
    def test_returns_success(self):
        response = self.client.get("/maps/flag_football")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "maps/activity.html")
        self.assertContains(response, MAPBOX_TOKEN)


class FootballViewTest(TestCase):
    def test_returns_success(self):
        response = self.client.get("/maps/football")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "maps/activity.html")
        self.assertContains(response, MAPBOX_TOKEN)


class FrisbeeViewTest(TestCase):
    def test_returns_success(self):
        response = self.client.get("/maps/frisbee")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "maps/activity.html")
        self.assertContains(response, MAPBOX_TOKEN)


class HandballViewTest(TestCase):
    def test_returns_success(self):
        response = self.client.get("/maps/handball")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "maps/activity.html")
        self.assertContains(response, MAPBOX_TOKEN)


class HockeyViewTest(TestCase):
    def test_returns_success(self):
        response = self.client.get("/maps/hockey")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "maps/activity.html")
        self.assertContains(response, MAPBOX_TOKEN)


class KickballViewTest(TestCase):
    def test_returns_success(self):
        response = self.client.get("/maps/kickball")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "maps/activity.html")
        self.assertContains(response, MAPBOX_TOKEN)


class LacrosseViewTest(TestCase):
    def test_returns_success(self):
        response = self.client.get("/maps/lacrosse")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "maps/activity.html")
        self.assertContains(response, MAPBOX_TOKEN)


class NetballViewTest(TestCase):
    def test_returns_success(self):
        response = self.client.get("/maps/netball")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "maps/activity.html")
        self.assertContains(response, MAPBOX_TOKEN)


class RugbyViewTest(TestCase):
    def test_returns_success(self):
        response = self.client.get("/maps/rugby")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "maps/activity.html")
        self.assertContains(response, MAPBOX_TOKEN)


class SoftballViewTest(TestCase):
    def test_returns_success(self):
        response = self.client.get("/maps/softball")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "maps/activity.html")
        self.assertContains(response, MAPBOX_TOKEN)


class TennisViewTest(TestCase):
    def test_returns_success(self):
        response = self.client.get("/maps/tennis")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "maps/activity.html")
        self.assertContains(response, MAPBOX_TOKEN)


class VolleyballViewTest(TestCase):
    def test_returns_success(self):
        response = self.client.get("/maps/volleyball")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "maps/activity.html")
        self.assertContains(response, MAPBOX_TOKEN)

class HikingViewTest(TestCase):
    def test_returns_success(self):
        response = self.client.get("/maps/hiking")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "maps/hiking.html")
        self.assertContains(response, MAPBOX_TOKEN)

# class FacilitiesViewTest(TestCase):
#     def test_returns_success(self):
#         response = self.client.get("/facilities/17308")
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, "maps/facilities.html")

#     def test_can_see_name(self):
#         response=self.client.get("/facilities/18627")
#         self.assertContains(response, "Bridge Park 3")

#     #decided that checking that response contains coords suffices
#     def test_can_see_lattitue(self):
#         response=self.client.get("/facilities/18627")
#         self.assertContains(response, "-73.98585882204912,40.70050871357319")
        
#     def test_can_see_sport(self):
#         response=self.client.get("/facilities/15184")
#         self.assertContains(response, "Baseball")

class MapsFacilitiesDataTest(TestCase):
    # test idea: checking if particular key (objectid) with a particular name is in parsed json file
    def test_returns_success(self):
        answer_dic = json.loads(read_facilities_data())
        answer_name = "Oakland Lake"
        self.assertEqual(answer_dic["13263"]["name"], answer_name)

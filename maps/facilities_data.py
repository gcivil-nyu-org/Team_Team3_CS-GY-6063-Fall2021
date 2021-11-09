import os
import json

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

script_dir = os.path.dirname(BASE_DIR)
file_path = os.path.join(BASE_DIR, "maps/athletic_facilities.json")
trails_file_path = os.path.join(BASE_DIR, "maps/hiking_trails.json")

def read_facilities_data():
    with open(file_path) as file:
        data = json.load(file)
        dic = {}
        res = {}
        for i in range(len(data["features"])):
            currentObj = data["features"][i]
            objId = currentObj["properties"]["objectid"]
            res[objId] = currentObj["properties"]
            res[objId]['geometry'] = currentObj['geometry']
        dic = res
        return json.dumps(dic)

def read_hiking_data():
    with open(trails_file_path) as file:
        data = json.load(file)
        dic = {}
        res = {}
        for i in range(len(data["features"])):
            currentObj = data["features"][i]
            objId = currentObj["properties"]["objectid"]
            res[objId] = currentObj["properties"]
        dic = res
        return json.dumps(dic)
    

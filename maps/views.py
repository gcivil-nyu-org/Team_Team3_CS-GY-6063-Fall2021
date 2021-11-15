from django.shortcuts import render
from config.settings import MAPBOX_TOKEN


def default_map(request):
    mapbox_access_token = MAPBOX_TOKEN
    return render(
        request, "maps/map.html", {"mapbox_access_token": mapbox_access_token}
    )

dataset = {
    'baseball' : 'ckvpcohczbjqi21ldh1w6tbvr',
    'basketball' : 'ckvpcn2q614yy20ml226c7urt',
    'bocce' : 'ckvpcowj71zsx27mrbhyeaoka',
    'cricket' : 'ckvpcp8djbvos21p76rbpyqgg',
    'flag_football' : 'ckvpcpjz99f3m27mnfmu5lfgx',
    'football' : 'ckvpcq22c6zdm27lfat21p1xp',
    'frisbee' : 'ckvpcqgsz9ufj27p98d3le32l',
    'handball' : 'ckvpcqv7zatvg20p9tkxil6m3',
    'hockey' : 'ckvpcrhes1ztu27mrqd6ok7za',
    'kickball' : 'ckvpcrvf72ctn21ldlj192jp0',
    'lacrosse' : 'ckvpcs8b66zeg27lfh10pn4ws',
    'netball' : 'ckvpcsnog24i222nr8v1a7hsk',
    'rugby' : 'ckvpct0cdkps722nzlsd8ubus',
    'softball' : 'ckvpcte3s9f4p27mnmakp0fxm',
    'tennis' : 'ckvpctv9022aa20mru7f9p1wk',
    'volleyball' : 'ckvpcuk449w2q27ldzs0qqjm2',
}

def activity_map(request):
    activity = request.resolver_match.url_name
    dataset_id = dataset[activity]
    mapbox_access_token = MAPBOX_TOKEN
    return render(
        request, "maps/activity.html", {"mapbox_access_token": mapbox_access_token, "dataset_id": dataset_id, "activity":activity}
    )

def hiking_map(request):
    mapbox_access_token = MAPBOX_TOKEN
    return render(
        request, "maps/hiking.html", {"mapbox_access_token": mapbox_access_token}
    )


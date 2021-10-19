from django.http import HttpResponse

def show(request, id):
    return HttpResponse(f'this will be the page for the facility with mapbox objectid: { id }')

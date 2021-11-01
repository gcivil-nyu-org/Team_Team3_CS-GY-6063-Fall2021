from django.shortcuts import render


def add_event(request):
    return render(
        request,
        "events/add_event.html",
    )

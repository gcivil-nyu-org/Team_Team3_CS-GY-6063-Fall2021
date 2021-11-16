from django.shortcuts import render
#connections_list = []

#for attendee in context['attendees']:
  #if attendee.user == self.request.user
    #add to connecitons list

def squad(request):
    return render(
        request,
        "squad/squad.html",
        {
            "key": "value",
        }
    )

from django.shortcuts import render
from events.models import Event, EventRegistration
#connections_list = []

#for attendee in context['attendees']:
  #if attendee.user == self.request.user
    #add to connecitons list
        #isAttending = False
    #context = super(EventDetailView, self).get_context_data(**kwargs)
    #context['attendees'] = EventRegistration.objects.filter(event = context["object"]);
    #for attendee in context['attendees']:
    #  if attendee.user == self.request.user:
    #    isAttending = True
    #context['isAttending'] = isAttending
    #return context

def squad(request):
    attendees_dupes = []
    attendees = []
    for er in EventRegistration.objects.filter(user = request.user):
        for er2 in EventRegistration.objects.filter(event = er.event).exclude(user = request.user):
            attendees_dupes.append(er2.user)
            [attendees.append(x) for x in attendees_dupes if x not in attendees]
    for e in Event.objects.filter(owner = request.user):
        for er in EventRegistration.objects.filter(event = e).exclude(user = request.user):
            attendees_dupes.append(er.user)
            [attendees.append(x) for x in attendees_dupes if x not in attendees] 
    #import pdb; pdb.set_trace()
    return render(
        request,
        "squad/squad.html",
        {
            "attendees": attendees,
        }
    )

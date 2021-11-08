from django.views.generic.base import TemplateView
from django.contrib.auth.decorators import login_required

from events.models import EventRegistration
    
class HomePageView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if(self.request.user.is_authenticated):
          context["events"] = EventRegistration.objects.filter(user = self.request.user)
        return context
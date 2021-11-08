from django.views.generic.base import TemplateView

from events.models import EventRegistration

class HomePageView(TemplateView):

    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["events"] = EventRegistration.objects.filter(user = self.request.user)
        return context
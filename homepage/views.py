from django.views.generic import TemplateView
from destinations.models import Destination
from packages.models import Activity, Package, SpecialEvent


class HomePageView(TemplateView):
    template_name = 'homepage/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        destinations = Destination.objects.all()
        activities = Activity.objects.all()
        packages = Package.objects.all()
        special_event = SpecialEvent.objects.filter(is_active=True).first()

        context['destinations'] = destinations
        context['activities'] = activities
        context['packages'] = packages
        context['special_event'] = special_event

        return context
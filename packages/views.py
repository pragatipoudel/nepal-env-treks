from django.views.generic import DetailView, ListView
from destinations.models import Destination
from .models import Package, Activity, SpecialEvent

class PackageDetailsView(DetailView):
    template_name = 'packages/details.html'
    model = Package
    context_object_name = 'package'
    

class PackageSearchView(ListView):
    template_name = 'packages/search.html'
    context_object_name = 'packages'
    paginate_by = 12

    def get_queryset(self):
        destination = self.request.GET.get('destination')
        activity = self.request.GET.get('activity')
        event_slug = self.kwargs.get('event_slug', None)

        packages = Package.objects.all()
        if destination:
            packages = packages.filter(destinations=destination)
        if activity:
            packages = packages.filter(activities=activity)
        if event_slug:
            packages = packages.filter(special_events__slug=event_slug)
        return packages

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['destinations'] = Destination.objects.all()
        context['activities'] = Activity.objects.all()

        destination = self.request.GET.get('destination', '')
        activity = self.request.GET.get('activity', '')
        event_slug = self.kwargs.get('event_slug', None)

        context['selected_destination'] = destination and int(destination)
        context['selected_activity'] = activity and int(activity)
        context['selected_event'] = event_slug and SpecialEvent.objects.get(slug=event_slug)

        context['query'] = f'destination={destination}&activity={activity}'

        return context

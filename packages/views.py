from typing import Any, Dict
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import DetailView, ListView
from destinations.models import Destination
from .models import Package, Activity

class PackageDetailsView(DetailView):
    template_name = 'packages/details.html'
    model = Package
    context_object_name = 'package'
    

class PackageSearchView(ListView):
    template_name = 'packages/search.html'
    context_object_name = 'packages'
    paginate_by = 6

    def get_queryset(self):
        destination = self.request.GET.get('destination')
        activity = self.request.GET.get('activity')

        packages = Package.objects.all()
        if destination:
            packages = packages.filter(destinations=destination)
        if activity:
            packages = packages.filter(activities=activity)
        return packages

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['destinations'] = Destination.objects.all()
        context['activities'] = Activity.objects.all()

        destination = self.request.GET.get('destination', '')
        activity = self.request.GET.get('activity', '')
        context['selected_destination'] = destination and int(destination)
        context['selected_activity'] = activity and int(activity)

        context['query'] = f'destination={destination}&activity={activity}'

        return context

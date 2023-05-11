from django.shortcuts import render
from django.views.generic import TemplateView
from django.db.models import Count
from destinations.models import Destination
from packages.models import Activity
from packages.models import Package


class HomePageView(TemplateView):
    template_name = 'homepage/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        destinations = Destination.objects.all()
        activities = Activity.objects.all()
        packages = Package.objects.all()

        context['destinations'] = destinations
        context['activities'] = activities
        context['packages'] = packages

        return context
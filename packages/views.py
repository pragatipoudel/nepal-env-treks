from django.shortcuts import render
from django.views.generic import DetailView, ListView
from .models import Package, FullItinerary, DailyItinerary

class PackageDetailsView(DetailView):
    template_name = 'packages/details.html'
    model = Package
    context_object_name = 'package'
    

class PackageSearchView(ListView):
    template_name = 'packages/search.html'
    model = Package
    context_object_name = 'package'
    
from django.shortcuts import render
from django.db.models import Count
from destinations.models import Destination
from packages.models import Activity
from packages.models import Package


def home_page(request):
    destinations = Destination.objects.annotate(package_count=Count('package'))
    activities = Activity.objects.all()
    packages = Package.objects.all()
    context = {
        'destinations': destinations,
        'activities': activities,
        'packages': packages,
    }
    return render(request, 'homepage/index.html', context)

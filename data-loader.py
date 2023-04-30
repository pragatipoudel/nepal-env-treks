import os
import json
import requests
import sys
from django.core import files
from django.core.files.base import ContentFile

from destinations.models import Destination
from packages.models import (
    Activity,
    Package,
    FullItinerary,
    DailyItinerary,
)


folder = 'scraped-data'
headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
}


def load_destination(destination_name):
    return Destination.objects.get_or_create(name=destination_name)[0]


def load_activity(activity_name):
    return Activity.objects.get_or_create(name=activity_name)[0]


def load_image(url):
    response = requests.get(url, headers=headers)
    if response.status_code != requests.codes.ok:
        print("could not load image from url", url)
        sys.exit(1)

    filename = url.split('/')[-1]
    return files.File(ContentFile(response.content), filename)


def load_package(destination, activity, package_details, num_days):
    title = package_details['title']
    overview = package_details['overview']
    image = load_image(package_details['image'])
    difficulty_level = package_details['grade']
    altitude = package_details['altitude']

    package = Package.objects.update_or_create(
        title=title,
        defaults={
            'overview': overview,
            'no_of_days': num_days,
            'header_image': image,
            'difficulty_level': difficulty_level,
            'altitude': altitude,
        }
    )[0]
    package.destinations.add(destination)
    package.activities.add(activity)

    return package


def load_itinerary(package, itinerary_data):
    full_itinerary = FullItinerary.objects.get_or_create(
        package=package
    )[0]
    
    for day_data in itinerary_data:
        day = day_data['day']
        max_day = day_data.get('max_day', None)
        title = day_data['title']
        details = day_data['details']
        elevation = day_data['elevation']
        duration = day_data['duration']

        DailyItinerary.objects.update_or_create(
            full_itinerary=full_itinerary,
            day=day,
            defaults={
                'title': title,
                'max_day': max_day,
                'details': details,
                'altitude': elevation,
                'duration': duration,
            }
        )


def load_from_file(file):
    data = json.load(open(file))
    
    destination = load_destination(data['destination'])
    activity = load_activity(data['activity'])
    itinerary = data['itinerary']
    package = load_package(destination, activity, data['package'], len(itinerary))

    load_itinerary(package, itinerary)


input_files = [file for file in os.listdir(folder) if file.endswith('.json')]

for file in input_files:
    print('Loading from', file)
    load_from_file(os.path.join(folder, file))

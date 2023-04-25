from django.db import models
from destinations.models import Destination

class Activity(models.Model):
    name = models.CharField(max_length=255)
    # header_image = 
    details = models.TextField()

    def __str__(self):
        return self.name

class Season(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Amenity(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name



class Package(models.Model):
    title = models.CharField(max_length=255)
    # header_image = 
    no_of_days = models.PositiveIntegerField()
    min_group_size = models.PositiveIntegerField(null=True, blank=True)
    max_group_size = models.PositiveIntegerField(null=True, blank=True)
    activities = models.ManyToManyField(Activity)
    difficulty_level = models.CharField(max_length=20, blank=True, choices=[
        ('easy', 'Easy'),
        ('moderate', 'Moderate'),
        ('difficult', 'Difficult')
    ])
    altitude = models.IntegerField(null=True, blank=True)
    rank = models.PositiveIntegerField(null=True, blank=True)
    seasons = models.ManyToManyField(Season, blank=True)
    overview = models.TextField()
    destinations = models.ManyToManyField(Destination)
    amenities = models.ManyToManyField(Amenity)

class FullItinerary(models.Model):
    package = models.OneToOneField(Package, on_delete=models.CASCADE)

class DailyItinerary(models.Model):
    title = models.CharField(max_length=255)
    duration = models.IntegerField()
    altitude = models.IntegerField(null=True, blank=True)
    details = models.TextField()
    full_itinerary = models.ForeignKey(FullItinerary, on_delete=models.CASCADE)

class PriceTier(models.Model):
    min_no_of_people = models.IntegerField(default=1)
    max_no_of_people = models.IntegerField(null=True, blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)


    





from django.db import models
from destinations.models import Destination

class Activity(models.Model):
    name = models.CharField(max_length=255)
    # header_image = 
    details = models.TextField()

class Season(models.Model):
    name = models.CharField(max_length=255)

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

    





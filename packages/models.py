from django.db import models
from destinations.models import Destination


class Activity(models.Model):
    name = models.CharField(max_length=255)
    header_image = models.ImageField(upload_to='images/destinations', null=True, blank=True)
    details = models.TextField(blank=True)
    rank = models.IntegerField(default=100)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Activities'
        ordering = ['rank']


class Season(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Amenity(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Amenities'


class Package(models.Model):
    title = models.CharField(max_length=255)
    header_image = models.ImageField(upload_to='images/destinations')
    no_of_days = models.PositiveIntegerField()
    min_group_size = models.PositiveIntegerField(null=True, blank=True)
    max_group_size = models.PositiveIntegerField(null=True, blank=True)
    activities = models.ManyToManyField(Activity)
    difficulty_level = models.CharField(max_length=20, null=True, blank=True, choices=[
        ('easy', 'Easy'),
        ('moderate', 'Moderate'),
        ('challenging', 'Challenging'),
        ('strenous', 'Strenous'),
    ])
    altitude = models.IntegerField(null=True, blank=True)
    rank = models.PositiveIntegerField(null=True, blank=True)
    seasons = models.ManyToManyField(Season, blank=True)
    overview = models.TextField()
    destinations = models.ManyToManyField(Destination)
    amenities = models.ManyToManyField(Amenity, blank=True)

    class Meta:
        ordering =  ['rank']

    def __str__(self):
        return self.title
    
    def min_price(self):
        return self.pricetier_set.first() and self.pricetier_set.first().price


class FullItinerary(models.Model):
    package = models.OneToOneField(Package, on_delete=models.CASCADE, related_name='full_itinerary')

    def __str__(self):
        return self.package.title

    class Meta:
        verbose_name_plural = 'Full Itineraries'


class DailyItinerary(models.Model):
    day = models.IntegerField()
    max_day = models.IntegerField(null=True, blank=True)
    title = models.CharField(max_length=255)
    duration = models.FloatField(null=True, blank=True)
    altitude = models.IntegerField(null=True, blank=True)
    details = models.TextField()
    full_itinerary = models.ForeignKey(FullItinerary, on_delete=models.CASCADE, related_name='daily_itineraries')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Daily Itineraries'
        ordering = ['day']
        unique_together = ('full_itinerary', 'day')



class PriceTier(models.Model):
    package = models.ForeignKey(Package, on_delete=models.CASCADE)
    min_no_of_people = models.IntegerField(default=1)
    max_no_of_people = models.IntegerField(null=True, blank=True)
    price = models.FloatField()

    def __str__(self):
        return f'{self.price} ({self.min_no_of_people} - {self.max_no_of_people})'
    
    class Meta:
        ordering = ['price']

from django.db import models
from django.core.validators import MinValueValidator
from datetime import date

class Inquiry(models.Model):
    title = models.CharField(max_length=255)
    no_of_people = models.IntegerField(validators=[MinValueValidator(0)])
    no_of_days = models.IntegerField(validators=[MinValueValidator(0)])
    start_date = models.DateField(null=True, blank=True, validators=[MinValueValidator(date.today)])
    name = models.CharField(max_length=255)
    contact_phone = models.CharField(max_length=20) 
    message = models.TextField(null=True, blank=True)

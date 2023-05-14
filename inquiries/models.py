from django.db import models
from django.core.validators import MinValueValidator
from phonenumber_field.modelfields import PhoneNumberField
from datetime import date

class Inquiry(models.Model):
    title = models.CharField(max_length=255)
    no_of_people = models.PositiveIntegerField()
    no_of_days = models.PositiveIntegerField(null=True, blank=True)
    contact_name = models.CharField(max_length=255)
    contact_email = models.EmailField(max_length=255)
    contact_phone = PhoneNumberField(max_length=20, blank=True)
    start_date = models.DateField(null=True, blank=True, validators=[MinValueValidator(date.today)])
    message = models.TextField(blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Inquiries'

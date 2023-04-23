from django.db import models

class Destination(models.Model):
    name = models.CharField(max_length=255)
    # header_image = 
    details = models.CharField(max_length=255)
    rank = models.PositiveIntegerField(default=1)

from django.db import models

class Destination(models.Model):
    name = models.CharField(max_length=255)
    header_image = models.ImageField(upload_to='images/destinations', null=True, blank=True)
    details = models.TextField(blank=True)
    rank = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.name

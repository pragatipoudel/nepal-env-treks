from django.db import models

class ContactInformation(models.Model):
    email = models.EmailField()
    mobile_phone = models.CharField(max_length=20)
    office_phone = models.CharField(max_length=20)
    fax = models.CharField(max_length=20)
    address = models.CharField(max_length=255)
    po_box = models.CharField(max_length=255)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name_plural = 'Contact Informations'

class Information(models.Model):
    key = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    details = models.TextField()

    def __str__(self):
        return self.title
from django.db import models

class Contact_info(models.Model):
    email = models.EmailField()
    mobile_phone = models.CharField(max_length=20)
    office_phone = models.CharField(max_length=20)
    fax = models.CharField(max_length=20)
    address = models.CharField(max_length=255)
    po_box = models.CharField(max_length=255)
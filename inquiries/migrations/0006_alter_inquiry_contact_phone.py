# Generated by Django 4.2 on 2023-05-14 00:07

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('inquiries', '0005_alter_inquiry_contact_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inquiry',
            name='contact_phone',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=20, region=None),
        ),
    ]

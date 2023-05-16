# Generated by Django 4.2 on 2023-05-13 23:55

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('inquiries', '0004_rename_name_inquiry_contact_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inquiry',
            name='contact_email',
            field=models.EmailField(max_length=255),
        ),
        migrations.AlterField(
            model_name='inquiry',
            name='contact_phone',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=20, region=None),
        ),
    ]
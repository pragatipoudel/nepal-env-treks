# Generated by Django 4.2 on 2023-05-20 03:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('packages', '0020_specialevent_name'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='dailyitinerary',
            unique_together=set(),
        ),
    ]
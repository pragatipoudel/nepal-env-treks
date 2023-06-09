# Generated by Django 4.2 on 2023-05-11 13:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('packages', '0013_alter_pricetier_options_alter_package_amenities'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='activity',
            options={'ordering': ['rank'], 'verbose_name_plural': 'Activities'},
        ),
        migrations.AddField(
            model_name='activity',
            name='rank',
            field=models.IntegerField(default=100),
        ),
        migrations.AlterField(
            model_name='dailyitinerary',
            name='full_itinerary',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='daily_itineraries', to='packages.fullitinerary'),
        ),
        migrations.AlterField(
            model_name='fullitinerary',
            name='package',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='full_itinerary', to='packages.package'),
        ),
        migrations.AlterUniqueTogether(
            name='dailyitinerary',
            unique_together={('full_itinerary', 'day')},
        ),
    ]

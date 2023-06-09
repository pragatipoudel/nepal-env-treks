# Generated by Django 4.2 on 2023-04-23 01:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('destinations', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('details', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Season',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Package',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('no_of_days', models.PositiveIntegerField()),
                ('min_group_size', models.PositiveIntegerField(blank=True, null=True)),
                ('max_group_size', models.PositiveIntegerField(blank=True, null=True)),
                ('difficulty_level', models.CharField(blank=True, choices=[('easy', 'Easy'), ('moderate', 'Moderate'), ('difficult', 'Difficult')], max_length=20)),
                ('altitude', models.IntegerField(blank=True, null=True)),
                ('rank', models.PositiveIntegerField(blank=True, null=True)),
                ('overview', models.TextField()),
                ('activities', models.ManyToManyField(to='packages.activity')),
                ('destinations', models.ManyToManyField(to='destinations.destination')),
                ('seasons', models.ManyToManyField(blank=True, to='packages.season')),
            ],
        ),
    ]

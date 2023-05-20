# Generated by Django 4.2 on 2023-05-20 01:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inquiries', '0007_eventadmininquiry'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='eventadmininquiry',
            name='id',
        ),
        migrations.AddField(
            model_name='eventadmininquiry',
            name='inquiry_ptr',
            field=models.OneToOneField(auto_created=True, default=None, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='inquiries.inquiry'),
            preserve_default=False,
        ),
    ]
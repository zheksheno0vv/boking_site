# Generated by Django 5.1.4 on 2024-12-15 10:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking_app', '0003_rename_start_hotel_hotel_start_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hotelphoto',
            name='photo',
        ),
        migrations.AddField(
            model_name='hotelphoto',
            name='hotel_photo',
            field=models.ImageField(blank=True, null=True, upload_to='hotel_photos/'),
        ),
        migrations.AlterField(
            model_name='hotelphoto',
            name='hotel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hotels', to='booking_app.hotel'),
        ),
    ]
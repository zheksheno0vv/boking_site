# Generated by Django 5.1.4 on 2024-12-12 11:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booking_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='country',
            old_name='country_name_tr',
            new_name='country_name_ru',
        ),
        migrations.RenameField(
            model_name='hotel',
            old_name='address_tr',
            new_name='address_ru',
        ),
        migrations.RenameField(
            model_name='hotel',
            old_name='city_tr',
            new_name='city_ru',
        ),
        migrations.RenameField(
            model_name='hotel',
            old_name='hotel_description_tr',
            new_name='hotel_description_ru',
        ),
        migrations.RenameField(
            model_name='hotel',
            old_name='hotel_name_tr',
            new_name='hotel_name_ru',
        ),
        migrations.RenameField(
            model_name='hotel',
            old_name='hotel_owner_tr',
            new_name='hotel_owner_ru',
        ),
        migrations.RenameField(
            model_name='room',
            old_name='room_description_tr',
            new_name='room_description_ru',
        ),
    ]
# Generated by Django 5.1.4 on 2024-12-19 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking_app', '0009_remove_review_review_stars_review_stars'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='stars',
            field=models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], max_length=16),
        ),
    ]

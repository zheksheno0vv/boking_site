# Generated by Django 5.1.4 on 2024-12-17 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking_app', '0005_alter_review_review_stars'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='review_stars',
            field=models.PositiveSmallIntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], max_length=16),
        ),
    ]
# Generated by Django 4.2 on 2023-05-31 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FayTourApp', '0037_hotel_coordinatesx_hotel_coordinatesy'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotel',
            name='coordinatesX',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='hotel',
            name='coordinatesY',
            field=models.FloatField(default=0.0),
        ),
    ]

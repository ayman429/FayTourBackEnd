# Generated by Django 4.2 on 2023-05-31 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FayTourApp', '0039_alter_hotel_coordinatesy'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotel',
            name='coordinatesY',
            field=models.FloatField(default=0.0),
        ),
    ]

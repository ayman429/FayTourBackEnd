# Generated by Django 4.2 on 2023-05-31 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FayTourApp', '0038_alter_hotel_coordinatesx_alter_hotel_coordinatesy'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotel',
            name='coordinatesY',
            field=models.FloatField(default=''),
        ),
    ]
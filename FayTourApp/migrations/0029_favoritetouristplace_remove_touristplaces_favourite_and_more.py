# Generated by Django 4.2 on 2023-05-26 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FayTourApp', '0028_favourite_touristplaces_favourite'),
    ]

    operations = [
        migrations.CreateModel(
            name='FavoriteTouristPlace',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PlaceId', models.CharField(max_length=500, unique=True)),
                ('name', models.CharField(max_length=500, unique=True)),
                ('image', models.CharField(max_length=1000, unique=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='touristplaces',
            name='favourite',
        ),
        migrations.DeleteModel(
            name='Favourite',
        ),
    ]
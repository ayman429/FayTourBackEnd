# Generated by Django 4.2 on 2023-05-26 20:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FayTourApp', '0031_alter_favorite_image_alter_favorite_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='favorite',
            old_name='PlaceId',
            new_name='userId',
        ),
    ]

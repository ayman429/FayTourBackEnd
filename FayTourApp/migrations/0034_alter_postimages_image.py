# Generated by Django 4.2 on 2023-05-30 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FayTourApp', '0033_delete_favorite'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postimages',
            name='image',
            field=models.ImageField(blank=True, default='', unique=True, upload_to='image/%y/%m/%d'),
        ),
    ]

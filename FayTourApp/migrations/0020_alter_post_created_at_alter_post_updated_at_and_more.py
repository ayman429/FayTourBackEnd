# Generated by Django 4.2 on 2023-05-22 22:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FayTourApp', '0019_alter_post_created_at_alter_post_updated_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 5, 23, 0, 52, 6, 740086), null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='updated_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 5, 23, 0, 52, 6, 740086), null=True),
        ),
        migrations.AlterField(
            model_name='postimages',
            name='image',
            field=models.ImageField(blank=True, unique=True, upload_to='image/%y/%m/%d'),
        ),
    ]

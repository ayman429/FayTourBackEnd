# Generated by Django 3.2.10 on 2023-06-22 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FayTourApp', '0042_auto_20230622_1534'),
    ]

    operations = [
        migrations.AddField(
            model_name='favorite',
            name='fav',
            field=models.BooleanField(default=False),
        ),
    ]

# Generated by Django 4.2 on 2023-05-22 23:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FayTourApp', '0023_alter_post_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['created_at']},
        ),
    ]
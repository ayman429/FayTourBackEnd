# Generated by Django 4.2 on 2023-05-20 01:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FayTourApp', '0005_post_postimage'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='description',
            new_name='body',
        ),
        migrations.RemoveField(
            model_name='post',
            name='title',
        ),
    ]

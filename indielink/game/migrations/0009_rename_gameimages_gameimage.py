# Generated by Django 4.2.7 on 2023-11-25 03:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0008_gameimages'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='GameImages',
            new_name='GameImage',
        ),
    ]
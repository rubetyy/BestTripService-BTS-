# Generated by Django 3.2.7 on 2021-09-27 06:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tour', '0010_rename_name_route_title'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Route_Touristspot',
            new_name='RouteTouristspot',
        ),
    ]
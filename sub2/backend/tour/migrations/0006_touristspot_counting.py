# Generated by Django 3.2.7 on 2021-09-20 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tour', '0005_alter_toruistimg_images'),
    ]

    operations = [
        migrations.AddField(
            model_name='touristspot',
            name='counting',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]

# Generated by Django 3.2.7 on 2021-09-20 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tour', '0004_review_toruistimg'),
    ]

    operations = [
        migrations.AlterField(
            model_name='toruistimg',
            name='images',
            field=models.TextField(),
        ),
    ]
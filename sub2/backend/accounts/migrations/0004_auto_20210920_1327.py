# Generated by Django 3.2.7 on 2021-09-20 04:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20210916_1121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='activity',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='age',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='budget',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='companion',
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='profile',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='selection',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='transportation',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='travelers',
            field=models.IntegerField(null=True),
        ),
    ]

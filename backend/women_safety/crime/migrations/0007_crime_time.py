# Generated by Django 3.0.4 on 2020-03-08 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crime', '0006_crime_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='crime',
            name='time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]

# Generated by Django 2.0.1 on 2018-01-22 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_country_url_imatge_bandera'),
    ]

    operations = [
        migrations.AddField(
            model_name='trip',
            name='route_trip_image',
            field=models.CharField(default='', help_text='Name of the image file saved in static ex: /images/trip.jpg', max_length=200),
        ),
    ]

# Generated by Django 2.0.1 on 2018-01-24 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_trip_route_trip_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='trip',
            name='url_static',
            field=models.CharField(default='', help_text='Route from the static folder ex (/static) /marroc (Just the /marroc)', max_length=200),
        ),
    ]

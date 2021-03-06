# Generated by Django 2.0.1 on 2019-08-09 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0017_remove_trip_route_trip_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plannedtrip',
            name='hero_image',
            field=models.ImageField(blank=True, help_text='Imatge hero', upload_to='plannedtrip'),
        ),
        migrations.AlterField(
            model_name='planstatusupdate',
            name='day_image',
            field=models.ImageField(blank=True, upload_to='plannedtripDay'),
        ),
        migrations.AlterField(
            model_name='redactor',
            name='hero_image',
            field=models.ImageField(blank=True, help_text='Imatge hero', upload_to='redactor'),
        ),
    ]

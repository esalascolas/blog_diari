# Generated by Django 2.0.1 on 2018-03-07 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_auto_20180218_1835'),
    ]

    operations = [
        migrations.AlterField(
            model_name='country',
            name='country_code',
            field=models.CharField(default='', max_length=3),
        ),
        migrations.AlterField(
            model_name='country',
            name='country_name',
            field=models.CharField(default='', max_length=100),
        ),
    ]

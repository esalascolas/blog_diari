# Generated by Django 2.0.1 on 2018-05-27 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0009_auto_20180527_1221'),
    ]

    operations = [
        migrations.AlterField(
            model_name='country',
            name='flag_image',
            field=models.ImageField(default='', upload_to='country'),
        ),
    ]
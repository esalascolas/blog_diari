# Generated by Django 2.0.1 on 2018-06-30 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0012_delete_document'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dayinstance',
            name='day_image',
            field=models.ImageField(blank=True, upload_to='day'),
        ),
    ]

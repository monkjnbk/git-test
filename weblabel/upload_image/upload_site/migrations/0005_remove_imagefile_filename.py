# Generated by Django 3.2.6 on 2021-08-12 13:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('upload_site', '0004_imagefile_filename'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='imagefile',
            name='filename',
        ),
    ]

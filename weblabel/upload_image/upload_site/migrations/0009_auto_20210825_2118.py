# Generated by Django 3.2.6 on 2021-08-25 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upload_site', '0008_auto_20210825_2110'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='ueser',
            new_name='user',
        ),
        migrations.AddField(
            model_name='imagefile',
            name='user',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]

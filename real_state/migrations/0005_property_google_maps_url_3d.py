# Generated by Django 3.2 on 2023-05-30 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('real_state', '0004_alter_property_google_maps_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='google_maps_url_3d',
            field=models.CharField(blank=True, max_length=500),
        ),
    ]

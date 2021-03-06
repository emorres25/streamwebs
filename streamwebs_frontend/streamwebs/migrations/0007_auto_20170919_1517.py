# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-09-19 15:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('streamwebs', '0006_auto_20170919_1350'),
    ]

    operations = [
        migrations.AlterField(
            model_name='camerapoint',
            name='map_datum',
            field=models.CharField(blank=True, choices=[(None, 'Not Recorded'), ('NAD27', 'NAD 27 CONUS'), ('NAD83', 'NAD 83'), ('WGS84', 'WGS84')], default=None, max_length=5, null=True, verbose_name='map datum'),
        ),
    ]

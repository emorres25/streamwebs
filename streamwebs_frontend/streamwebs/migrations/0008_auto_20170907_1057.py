# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-09-07 10:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('streamwebs', '0007_auto_20170907_1016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='water_quality',
            name='air_temp_unit',
            field=models.CharField(choices=[('Fahrenheit', 'Fahrenheit'), ('Celsius', 'Celsius')], default=0, max_length=255, null=True, verbose_name='air temperature units'),
        ),
        migrations.AlterField(
            model_name='water_quality',
            name='water_temp_unit',
            field=models.CharField(choices=[('Fahrenheit', 'Fahrenheit'), ('Celsius', 'Celsius')], default=0, max_length=255, null=True, verbose_name='water temperature units'),
        ),
    ]
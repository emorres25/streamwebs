# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-09-13 14:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('streamwebs', '0012_auto_20170913_1439'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='canopy_cover',
            name='date',
        ),
        migrations.RemoveField(
            model_name='canopy_cover',
            name='time',
        ),
        migrations.AddField(
            model_name='canopy_cover',
            name='date_time',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='date and time'),
        ),
    ]
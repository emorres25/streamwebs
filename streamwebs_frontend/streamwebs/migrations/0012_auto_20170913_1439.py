# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-09-13 14:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('streamwebs', '0011_auto_20170913_1225'),
    ]

    operations = [
        migrations.AlterField(
            model_name='canopy_cover',
            name='time',
            field=models.TimeField(default=b'14:39'),
        ),
    ]
# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-09-19 12:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('streamwebs', '0004_auto_20170831_1428'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photopoint',
            name='camera_height',
            field=models.DecimalField(blank=True, decimal_places=0, max_digits=3, null=True, verbose_name='camera height'),
        ),
        migrations.AlterField(
            model_name='photopoint',
            name='distance',
            field=models.DecimalField(blank=True, decimal_places=0, max_digits=3, null=True, verbose_name='distance from camera point'),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-19 21:16
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('streamwebs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='birthdate',
            field=models.DateField(default=datetime.date(1999, 4, 1)),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='school',
            field=models.CharField(choices=[('a', 'School A'), ('b', 'School B'), ('c', 'School C')], default='', max_length=1),
        ),
    ]
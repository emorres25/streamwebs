# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-20 20:15
from __future__ import unicode_literals

from django.db import migrations, models
import streamwebs.models


class Migration(migrations.Migration):

    dependencies = [
        ('streamwebs', '0002_auto_20160519_1416'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='school',
            field=models.CharField(choices=[('a', 'School A'), ('b', 'School B'), ('c', 'School C')], default='', max_length=1, validators=[streamwebs.models.validate_UserProfile_school]),
        ),
    ]

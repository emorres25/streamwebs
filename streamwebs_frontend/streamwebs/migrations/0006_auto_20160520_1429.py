# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-20 21:29
from __future__ import unicode_literals

from django.db import migrations, models
import streamwebs.models


class Migration(migrations.Migration):

    dependencies = [
        ('streamwebs', '0005_auto_20160520_1428'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='birthdate',
            field=models.DateField(validators=[streamwebs.models.validate_UserProfile_birthdate]),
        ),
    ]
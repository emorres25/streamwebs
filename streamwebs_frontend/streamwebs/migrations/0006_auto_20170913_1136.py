# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-09-13 11:36
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('streamwebs', '0005_ripaquaticsurvey'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ripaquaticsurvey',
            old_name='widlife_type',
            new_name='wildlife_type',
        ),
    ]

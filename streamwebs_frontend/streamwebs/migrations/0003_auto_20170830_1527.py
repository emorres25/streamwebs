# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-08-30 15:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('streamwebs', '0002_auto_20170817_1610'),
    ]

    operations = [
        migrations.AlterField(
            model_name='school',
            name='school_type',
            field=models.CharField(choices=[('Elementary School', 'Elementary School'), ('Middle School', 'Middle School'), ('High School', 'High School'), ('Organization', 'Organization'), ('Community College', 'Community College'), ('State College', 'State College')], default=0, max_length=250, null=True, verbose_name='school type'),
        ),
    ]

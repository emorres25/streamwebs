# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-08-31 14:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('streamwebs', '0003_auto_20170830_1527'),
    ]

    operations = [
        migrations.AlterField(
            model_name='school',
            name='address',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='school',
            name='city',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='school',
            name='province',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='school',
            name='zipcode',
            field=models.CharField(max_length=250),
        ),
    ]

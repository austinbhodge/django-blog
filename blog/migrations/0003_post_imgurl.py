# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-20 12:45
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20160320_0709'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='imgUrl',
            field=models.CharField(default=datetime.datetime(2016, 3, 20, 12, 45, 56, 392136, tzinfo=utc), max_length=300),
            preserve_default=False,
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-20 03:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0003_report'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='path',
            field=models.CharField(default='', max_length=100),
        ),
    ]
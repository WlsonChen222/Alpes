# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-17 05:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bundle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('programId', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Firmware',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('version', models.CharField(max_length=100)),
                ('category', models.CharField(max_length=10)),
                ('bundleId', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Program',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='software',
            name='bundleId',
            field=models.IntegerField(default=0),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-23 05:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oddslingers', '0009_auto_20170921_2257'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='bio',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='profile_picture',
            field=models.CharField(blank=True, max_length=32, null=True),
        ),
    ]
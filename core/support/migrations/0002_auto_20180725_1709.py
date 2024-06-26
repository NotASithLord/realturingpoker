# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-07-25 17:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('support', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='supportticket',
            name='source',
            field=models.CharField(choices=[('admin', 'Admin Created'), ('email', 'Email to support@turingpoker.com'), ('support-page', 'Support Page Submition'), ('table-report-bug', 'Report Bug on a Table'), ('heartbeat', 'Heartbeat Exception'), ('botbeat', 'Botbeat Exception')], default='admin', max_length=32),
        ),
        migrations.AlterField(
            model_name='supportticket',
            name='subject',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2018-01-03 13:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0015_auto_20171117_2013'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='token',
            field=models.CharField(blank=True, max_length=100, null=True, unique=True, verbose_name='Token'),
        ),
    ]

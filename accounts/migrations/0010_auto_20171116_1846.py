# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-11-16 18:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_auto_20171116_1747'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='active'),
        ),
    ]
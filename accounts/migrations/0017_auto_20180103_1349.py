# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2018-01-03 13:49
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0016_account_token'),
    ]

    operations = [
        migrations.RenameField(
            model_name='account',
            old_name='token',
            new_name='github_token',
        ),
    ]

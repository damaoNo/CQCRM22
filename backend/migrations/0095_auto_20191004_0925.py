# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2019-10-04 09:25
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0094_auto_20191004_0851'),
    ]

    operations = [
        migrations.RenameField(
            model_name='treat',
            old_name='isAppoint',
            new_name='isappoint',
        ),
    ]
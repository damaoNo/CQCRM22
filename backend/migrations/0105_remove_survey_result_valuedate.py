# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2019-10-11 22:58
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0104_survey_result'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='survey_result',
            name='valuedate',
        ),
    ]
# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2019-09-12 16:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0034_auto_20190911_2131'),
    ]

    operations = [
        migrations.AddField(
            model_name='project_dict',
            name='flag',
            field=models.BooleanField(default=0, verbose_name='是否为系统套餐'),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2019-09-29 17:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0080_auto_20190929_1718'),
    ]

    operations = [
        migrations.AlterField(
            model_name='treat',
            name='treattype',
            field=models.SmallIntegerField(blank=True, default=0, null=True, verbose_name='检测类型'),
        ),
    ]

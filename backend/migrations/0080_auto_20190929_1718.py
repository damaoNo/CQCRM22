# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2019-09-29 17:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0079_auto_20190929_1527'),
    ]

    operations = [
        migrations.AlterField(
            model_name='treat',
            name='healthtype',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='健康类型'),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2019-10-01 07:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0084_auto_20191001_0717'),
    ]

    operations = [
        migrations.AlterField(
            model_name='treat',
            name='operatedate',
            field=models.DateField(blank=True, null=True, verbose_name='操作日期'),
        ),
    ]
# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2019-09-26 15:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0072_auto_20190926_1454'),
    ]

    operations = [
        migrations.AlterField(
            model_name='treat',
            name='operatedate',
            field=models.DateField(auto_now_add=True, null=True, verbose_name='操作日期'),
        ),
    ]
# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2019-09-17 12:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0057_auto_20190916_1050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='issuccess',
            field=models.SmallIntegerField(default=1, verbose_name='宣教是否成功'),
        ),
    ]
# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2019-10-02 11:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0090_auto_20191002_1155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='callback',
            name='execute',
            field=models.SmallIntegerField(default=0, verbose_name='执行情况'),
        ),
    ]

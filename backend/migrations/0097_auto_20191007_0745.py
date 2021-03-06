# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2019-10-07 07:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0096_survey'),
    ]

    operations = [
        migrations.AddField(
            model_name='treat',
            name='energy',
            field=models.FloatField(blank=True, null=True, verbose_name='治疗能量'),
        ),
        migrations.AddField(
            model_name='treat',
            name='report',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='评估报告'),
        ),
        migrations.AddField(
            model_name='treat',
            name='wendu',
            field=models.FloatField(blank=True, null=True, verbose_name='温度'),
        ),
        migrations.AddField(
            model_name='treat',
            name='yaling',
            field=models.SmallIntegerField(default=0, verbose_name='是否使用引导哑铃'),
        ),
    ]

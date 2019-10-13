# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2019-09-11 07:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0022_performance_dict'),
    ]

    operations = [
        migrations.CreateModel(
            name='performance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(blank=True, max_length=500, null=True, verbose_name='备注')),
                ('hrmdepartment', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='backend.HrmDepartment', verbose_name='中心id')),
                ('performancedict', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='backend.performance_dict', verbose_name='绩效id')),
            ],
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2019-09-13 20:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0045_auto_20190913_1712'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tuitionfee_detail',
            name='project',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='backend.project', verbose_name='项目id'),
        ),
    ]

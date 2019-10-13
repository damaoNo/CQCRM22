# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2019-09-15 15:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0054_client_register_diagnose'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client_jinjizheng',
            name='client',
        ),
        migrations.AddField(
            model_name='client_jinjizheng',
            name='clientregister',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='backend.client_register', verbose_name='客户登记id'),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2019-09-20 09:54
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0066_auto_20190919_2144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='treat',
            name='adduser',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='adduser_treat', to=settings.AUTH_USER_MODEL, verbose_name='开单人id'),
        ),
        migrations.AlterField(
            model_name='treat',
            name='operator',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='operate_user', to=settings.AUTH_USER_MODEL, verbose_name='操作人id'),
        ),
        migrations.AlterField(
            model_name='treat',
            name='order',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='backend.order', verbose_name='订单id'),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2019-10-02 09:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0088_callback_callbacktype'),
    ]

    operations = [
        migrations.AddField(
            model_name='callback',
            name='isacquire',
            field=models.SmallIntegerField(default=0, verbose_name='是否收单'),
        ),
    ]

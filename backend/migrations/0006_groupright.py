# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2019-09-08 15:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
        ('backend', '0005_sysright'),
    ]

    operations = [
        migrations.CreateModel(
            name='GroupRight',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isvisible', models.BooleanField(default=1)),
                ('group', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='auth.Group', verbose_name='角色')),
                ('rights', models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, to='backend.sysRight', verbose_name='权限')),
            ],
        ),
    ]

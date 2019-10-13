# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2019-09-08 14:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Menus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('url_type', models.SmallIntegerField(choices=[(0, 'absolute'), (1, 'dynamic')], default=0)),
                ('path', models.CharField(default='', max_length=128)),
                ('parent_id', models.CharField(blank=True, max_length=20, null=True)),
                ('menu_id', models.IntegerField(blank=True, default='', null=True)),
            ],
        ),
    ]

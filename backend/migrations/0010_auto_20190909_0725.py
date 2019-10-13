# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2019-09-09 07:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0009_coo_hospital'),
    ]

    operations = [
        migrations.CreateModel(
            name='invoice_dict',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='名称')),
                ('comment', models.CharField(blank=True, max_length=500, null=True, verbose_name='备注')),
            ],
        ),
        migrations.CreateModel(
            name='invoice_set',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('invoice_id', models.IntegerField(blank=True, default=1, null=True, verbose_name='开票名称')),
                ('profit_distri_id', models.IntegerField(blank=True, default=1, null=True, verbose_name='利润分成')),
                ('begindate', models.DateField(blank=True, null=True, verbose_name='开始日期')),
                ('enddate', models.DateField(blank=True, null=True, verbose_name='结束日期')),
                ('value', models.FloatField(blank=True, default=0, null=True, verbose_name='数值')),
                ('comment', models.CharField(blank=True, max_length=500, null=True, verbose_name='备注')),
                ('hospital', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='hzhospital', to='backend.coo_hospital', verbose_name='合作医院')),
            ],
        ),
        migrations.CreateModel(
            name='profit_distri_dict',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='名称')),
                ('comment', models.CharField(blank=True, max_length=500, null=True, verbose_name='备注')),
            ],
        ),
        migrations.AlterModelOptions(
            name='permission',
            options={'permissions': (('coo_hospital', '合作医院'), ('organization', '组织机构设置'), ('xlog', '操作日志'))},
        ),
    ]

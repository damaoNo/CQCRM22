# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2019-09-10 16:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0017_auto_20190910_1123'),
    ]

    operations = [
        migrations.CreateModel(
            name='finance_month',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True, verbose_name='月份')),
                ('comment', models.CharField(blank=True, max_length=500, null=True, verbose_name='备注')),
                ('hrmdepartment', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='backend.HrmDepartment', verbose_name='中心id')),
            ],
        ),
        migrations.AlterModelOptions(
            name='permission',
            options={'permissions': (('finance_month', '财务月'), ('coo_hospital', '合作医院'), ('dept_dict', '科室字典'), ('post_dict', '岗位字典'), ('dept', '中心科室'), ('organization', '组织机构设置'), ('xlog', '操作日志'))},
        ),
    ]

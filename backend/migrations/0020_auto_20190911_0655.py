# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2019-09-11 06:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0019_auto_20190910_2217'),
    ]

    operations = [
        migrations.CreateModel(
            name='tuition_dict',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='名称')),
                ('comment', models.CharField(blank=True, max_length=500, null=True, verbose_name='备注')),
            ],
        ),
        migrations.CreateModel(
            name='tuitionFee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.FloatField(default=0, verbose_name='数值')),
                ('comment', models.CharField(blank=True, max_length=500, null=True, verbose_name='备注')),
                ('deptdict', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='backend.dept_dict', verbose_name='科室id')),
                ('hrmdepartment', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='backend.HrmDepartment', verbose_name='中心id')),
                ('tuition', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='backend.tuition_dict', verbose_name='带教费类型id')),
            ],
        ),
        migrations.AlterModelOptions(
            name='permission',
            options={'permissions': (('tuitionFee', '带教费'), ('tuition_dict', '带教费类型'), ('project_dict', '项目字典'), ('finance_month', '财务月'), ('coo_hospital', '合作医院'), ('dept_dict', '科室字典'), ('post_dict', '岗位字典'), ('dept', '中心科室'), ('organization', '组织机构设置'), ('xlog', '操作日志'))},
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2019-10-11 14:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0100_survey_title_survey_title_answer'),
    ]

    operations = [
        migrations.CreateModel(
            name='treat_survey',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adddate', models.DateField(auto_now_add=True, verbose_name='添加日期')),
                ('comment', models.CharField(blank=True, max_length=500, null=True, verbose_name='备注')),
                ('adduser', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='backend.userProfile', verbose_name='添加人id')),
                ('survey', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='backend.survey', verbose_name='问卷id')),
                ('treat', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='backend.treat', verbose_name='治疗id')),
            ],
        ),
    ]

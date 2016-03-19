# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-12 23:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='description',
            field=models.TextField(blank=True, verbose_name='\u043a\u043e\u0440\u043e\u0442\u043a\u0438\u0439 \u043e\u043f\u0438\u0441'),
        ),
        migrations.AlterField(
            model_name='post',
            name='datetime',
            field=models.DateTimeField(verbose_name='\u0414\u0430\u0442\u0430 \u043f\u0443\u0431\u043b\u0456\u043a\u0430\u0446\u0456\u0457'),
        ),
    ]
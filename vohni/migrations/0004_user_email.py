# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-21 14:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vohni', '0003_auto_20160320_1221'),
    ]

    operations = [
        migrations.CreateModel(
            name='User_Email',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.URLField(blank=True, null=True, verbose_name='\u0435\u043c\u0435\u0439\u043b\u0438 \u043a\u043e\u0440\u0438\u0441\u0442\u0443\u0432\u0430\u0447\u0456\u0432')),
            ],
            options={
                'verbose_name': '\u0435\u043c\u0435\u0439\u043b \u043a\u043e\u0440\u0438\u0441\u0442\u0443\u0432\u0430\u0447\u0430',
                'verbose_name_plural': '\u0435\u043c\u0435\u0439\u043b\u0438 \u043a\u043e\u0440\u0438\u0441\u0442\u0443\u0432\u0430\u0447\u0456\u0432',
            },
        ),
    ]
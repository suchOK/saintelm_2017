# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-21 23:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vohni', '0007_remove_user_email_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_email',
            name='name',
            field=models.CharField(max_length=256, null=True, verbose_name="\u0412\u0430\u0448\u0435 \u0456\u043c'\u044f"),
        ),
    ]

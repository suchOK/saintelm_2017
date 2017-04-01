# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vohni', '0004_auto_20170401_1300'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='day',
            name='journey',
        ),
        migrations.AddField(
            model_name='journey',
            name='day',
            field=models.ManyToManyField(default='', to='vohni.Day', blank=True, verbose_name='опис мандрівного дня'),
        ),
        migrations.AlterField(
            model_name='day',
            name='title_day',
            field=models.CharField(verbose_name='назва дня', max_length=256),
        ),
    ]

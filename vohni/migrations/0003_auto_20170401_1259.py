# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vohni', '0002_auto_20170401_1247'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='journey',
            name='day',
        ),
        migrations.AddField(
            model_name='day',
            name='journey',
            field=models.ForeignKey(blank=True, verbose_name='мандрівка', to='vohni.Journey', default=''),
        ),
        migrations.AlterField(
            model_name='day',
            name='title_day',
            field=models.CharField(max_length=256, verbose_name='назва дня'),
        ),
    ]

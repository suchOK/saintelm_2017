# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vohni', '0003_auto_20170401_1259'),
    ]

    operations = [
        migrations.AlterField(
            model_name='day',
            name='title_day',
            field=models.CharField(max_length=256, verbose_name='назва дня', blank=True),
        ),
    ]

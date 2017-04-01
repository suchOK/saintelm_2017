# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vohni', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='day',
            name='title_day',
            field=models.CharField(verbose_name='назва дня', max_length=256, blank=True),
        ),
    ]

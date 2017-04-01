# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vohni', '0007_auto_20170401_1322'),
    ]

    operations = [
        migrations.AlterField(
            model_name='day',
            name='date_day',
            field=models.DateField(verbose_name='дата дня'),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vohni', '0005_auto_20170401_1306'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='day',
            options={'verbose_name_plural': 'Дні', 'verbose_name': 'День'},
        ),
        migrations.RemoveField(
            model_name='day',
            name='order_in_journey',
        ),
    ]

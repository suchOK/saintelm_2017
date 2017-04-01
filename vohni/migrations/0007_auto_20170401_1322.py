# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vohni', '0006_auto_20170401_1316'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='day',
            options={'verbose_name_plural': 'Дні', 'ordering': ['date_day'], 'verbose_name': 'День'},
        ),
        migrations.AddField(
            model_name='day',
            name='date_day',
            field=models.IntegerField(default=1, verbose_name='дата дня'),
            preserve_default=False,
        ),
    ]

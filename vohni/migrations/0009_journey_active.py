# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vohni', '0008_auto_20170401_1323'),
    ]

    operations = [
        migrations.AddField(
            model_name='journey',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]

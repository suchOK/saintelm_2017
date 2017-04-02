# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vohni', '0009_journey_active'),
    ]

    operations = [
        migrations.CreateModel(
            name='CoverImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('cover_image_url', models.CharField(verbose_name='посилання', blank=True, max_length=200, null=True)),
            ],
            options={
                'verbose_name': 'фото на головній',
            },
        ),
    ]

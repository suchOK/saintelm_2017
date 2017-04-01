# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('title', models.CharField(max_length=256, verbose_name='назва поста')),
                ('datetime', models.DateTimeField(verbose_name='Дата публікації')),
                ('description', tinymce.models.HTMLField(verbose_name='короткий опис', blank=True)),
                ('text', tinymce.models.HTMLField(verbose_name='текст', blank=True)),
                ('blog_photo', models.ImageField(null=True, upload_to='', verbose_name='фото', blank=True)),
            ],
            options={
                'verbose_name': 'Пост',
                'verbose_name_plural': 'Пости',
            },
        ),
    ]

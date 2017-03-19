# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=256, verbose_name='назва поста')),
                ('datetime', models.DateTimeField(verbose_name='Дата публікації')),
                ('description', models.TextField(blank=True, verbose_name='короткий опис')),
                ('text', models.TextField(blank=True, verbose_name='текст')),
                ('blog_photo', models.ImageField(blank=True, verbose_name='фото', upload_to='', null=True)),
            ],
            options={
                'verbose_name_plural': 'Пости',
                'verbose_name': 'Пост',
            },
        ),
    ]

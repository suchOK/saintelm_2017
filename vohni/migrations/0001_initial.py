# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('photologue', '0010_auto_20160105_1307'),
    ]

    operations = [
        migrations.CreateModel(
            name='Day',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('title_day', models.CharField(max_length=256, verbose_name='назва дня')),
                ('description', tinymce.models.HTMLField(verbose_name='опис дня', blank=True)),
                ('order_in_journey', models.IntegerField(verbose_name='порядковий номер у мандрівці')),
            ],
            options={
                'ordering': ['order_in_journey'],
                'verbose_name': 'День',
                'verbose_name_plural': 'Дні',
            },
        ),
        migrations.CreateModel(
            name='Journey',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('title', models.CharField(max_length=256, verbose_name='назва мандрівки')),
                ('slug', models.SlugField(max_length=100, unique=True)),
                ('describe', tinymce.models.HTMLField(verbose_name='короткий опис', blank=True)),
                ('cities', tinymce.models.HTMLField(max_length=256, verbose_name='міста')),
                ('price', models.CharField(default='', max_length=256, verbose_name='ціна', blank=True)),
                ('start_date', models.DateField(null=True, verbose_name='початок мандрівки')),
                ('end_date', models.DateField(null=True, verbose_name='кінець мандрівки')),
                ('main_photo', models.ImageField(null=True, upload_to='', verbose_name='фото', blank=True)),
                ('conditions', tinymce.models.HTMLField(verbose_name='умови', blank=True)),
                ('documents', tinymce.models.HTMLField(verbose_name='документи', blank=True)),
                ('options', tinymce.models.HTMLField(null=True, verbose_name='додаткові опції', blank=True)),
                ('price_include', tinymce.models.HTMLField(null=True, verbose_name='у вартість входить', blank=True)),
                ('price_not_include', tinymce.models.HTMLField(null=True, verbose_name='у вартість не входить', blank=True)),
                ('donation', tinymce.models.HTMLField(null=True, verbose_name='пожертва', blank=True)),
                ('day', models.ForeignKey(blank=True, to='vohni.Day', default='', verbose_name='опис мандрівного дня')),
                ('gallery', models.ForeignKey(related_name='gallery', blank=True, on_delete=django.db.models.deletion.SET_NULL, null=True, to='photologue.Gallery', verbose_name='фотки')),
            ],
            options={
                'verbose_name': 'Мандрівка',
                'verbose_name_plural': 'Мандрівки',
            },
        ),
        migrations.CreateModel(
            name='User_Email',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('email', models.EmailField(null=True, max_length=200, verbose_name='Ваш email')),
                ('name', models.CharField(null=True, max_length=256, verbose_name="Ваше ім'я та номер телефону")),
                ('journey_choice', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.SET_NULL, null=True, to='vohni.Journey', verbose_name='Мандрівка')),
            ],
            options={
                'verbose_name': 'емейл користувача',
                'verbose_name_plural': 'емейли користувачів',
            },
        ),
    ]

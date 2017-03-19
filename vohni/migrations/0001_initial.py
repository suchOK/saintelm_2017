# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('photologue', '0010_auto_20160105_1307'),
    ]

    operations = [
        migrations.CreateModel(
            name='Day',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('title_day', models.CharField(max_length=256, verbose_name='назва дня')),
                ('description', models.TextField(blank=True, verbose_name='опис дня')),
            ],
        ),
        migrations.CreateModel(
            name='Journey',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=256, verbose_name='назва мандрівки')),
                ('slug', models.SlugField(max_length=100, unique=True)),
                ('describe', models.TextField(blank=True, verbose_name='короткий опис')),
                ('cities', models.CharField(max_length=256, verbose_name='міста')),
                ('price', models.CharField(blank=True, max_length=256, verbose_name='ціна', default='')),
                ('start_date', models.DateField(verbose_name='початок мандрівки', null=True)),
                ('end_date', models.DateField(verbose_name='кінець мандрівки', null=True)),
                ('main_photo', models.ImageField(blank=True, verbose_name='фото', upload_to='', null=True)),
                ('conditions', models.TextField(blank=True, verbose_name='умови')),
                ('documents', models.TextField(blank=True, verbose_name='документи')),
                ('options', models.TextField(blank=True, verbose_name='додаткові опції', null=True)),
                ('price_include', models.TextField(blank=True, verbose_name='у вартість входить', null=True)),
                ('price_not_include', models.TextField(blank=True, verbose_name='у вартість не входить', null=True)),
                ('donation', models.TextField(blank=True, verbose_name='пожертва', null=True)),
                ('day', models.ManyToManyField(blank=True, to='vohni.Day', verbose_name='опис мандрівного дня', default='')),
                ('gallery', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.SET_NULL, to='photologue.Gallery', null=True, related_name='gallery', verbose_name='фотки')),
            ],
            options={
                'verbose_name_plural': 'Мандрівки',
                'verbose_name': 'Мандрівка',
            },
        ),
        migrations.CreateModel(
            name='User_Email',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=200, verbose_name='Ваш email', null=True)),
                ('name', models.CharField(max_length=256, verbose_name="Ваше ім'я", null=True)),
                ('journey_choice', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.SET_NULL, to='vohni.Journey', null=True, verbose_name='Мандрівка')),
            ],
            options={
                'verbose_name_plural': 'емейли користувачів',
                'verbose_name': 'емейл користувача',
            },
        ),
    ]

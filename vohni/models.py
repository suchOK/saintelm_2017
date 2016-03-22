# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models
from photologue.models import Gallery

# Create your models here.

class Journey(models.Model):
    """Journey Model"""

    class Meta(object):
        verbose_name = u"Мандрівка"
        verbose_name_plural = u"Мандрівки"

    title = models.CharField(
        max_length=256,
        blank=False,
        verbose_name=u"назва мандрівки")

    gallery = models.ForeignKey('photologue.Gallery',
        verbose_name=u"фотки",
        blank=True,
        null=True,
        related_name='gallery',
        on_delete=models.SET_NULL)

    describe = models.TextField(
        blank=True,
        verbose_name=u"короткий опис")

    cities = models.CharField(
        max_length=256,
        blank=False,
        verbose_name=u"міста")

    price = models.CharField(
        max_length=256,
        blank=True,
        verbose_name=u"ціна",
        default='')

    start_date = models.DateField(
        blank=False,
        verbose_name=u"початок мандрівки",
        null=True)

    end_date = models.DateField(
        blank=False,
        verbose_name=u"кінець мандрівки",
        null=True)

    main_photo = models.ImageField(
        blank=True,
        verbose_name=u"фото",
        null=True)

    roadmap = models.TextField(
        blank=True,
        verbose_name=u"маршрут")

    day_1 = models.ForeignKey('day1',
        blank=True,
        null=True,
        default='',
        verbose_name=u"опис першого дня")

    day_2 = models.ForeignKey('day2',
        blank=True,
        null=True,
        default='',
        verbose_name=u"опис другого дня")

    day_3 = models.ForeignKey('day3',
        blank=True,
        null=True,
        default='',
        verbose_name=u"опис третього дня")

    day_4 = models.ForeignKey('day4',
        blank=True,
        null=True,
        default='',
        verbose_name=u"опис четвертого дня")

    day_5 = models.ForeignKey('day5',
        blank=True,
        null=True,
        default='',
        verbose_name=u"опис п*ятого дня")

    day_6 = models.ForeignKey('day6',
        blank=True,
        null=True,
        default='',
        verbose_name=u"опис шостого дня")

    day_7 = models.ForeignKey('day7',
        blank=True,
        null=True,
        default='',
        verbose_name=u"опис сьомого дня")

    day_8 = models.ForeignKey('day8',
        blank=True,
        null=True,
        default='',
        verbose_name=u"опис восьмого дня")

    conditions = models.TextField(
        blank=True,
        verbose_name=u"умови")

    documents = models.TextField(
        blank=True,
        verbose_name=u"документи")

    options = models.TextField(
        blank=True,
        null=True,
        verbose_name=u"додаткові опції")

    price_include = models.TextField(
        blank=True,
        null=True,
        verbose_name=u"у вартість входить")

    price_not_include = models.TextField(
        blank=True,
        null=True,
        verbose_name=u"у вартість не входить")

    donation = models.TextField(
        blank=True,
        null=True,
        verbose_name=u"пожертва")


    def __unicode__(self):
        return u"%s %s" % (self.title, self.cities)


class day1(models.Model):

    title_day1 = models.CharField(
        max_length=256,
        blank=False,
        verbose_name=u"назва першого дня")
    day1 = models.TextField(
        blank=True,
        verbose_name=u"опис першого дня")

    def __unicode__(self):
        return u"%s %s" % (self.title_day1, self.day1)

class day2(models.Model):

    title_day2 = models.CharField(
        max_length=256,
        blank=False,
        verbose_name=u"назва другого дня")
    day2 = models.TextField(
        blank=True,
        verbose_name=u"опис другого дня")

    def __unicode__(self):
        return u"%s %s" % (self.title_day2, self.day2)

class day3(models.Model):

    title_day3 = models.CharField(
        max_length=256,
        blank=False,
        verbose_name=u"назва третього дня")
    day3 = models.TextField(
        blank=True,
        verbose_name=u"опис третього дня")

    def __unicode__(self):
        return u"%s %s" % (self.title_day3, self.day3)

class day4(models.Model):

    title_day4 = models.CharField(
        max_length=256,
        blank=False,
        verbose_name=u"назва четвертого дня")
    day4 = models.TextField(
        blank=True,
        verbose_name=u"опис четвертого дня")

    def __unicode__(self):
        return u"%s %s" % (self.title_day4, self.day4)

class day5(models.Model):

    title_day5 = models.CharField(
        max_length=256,
        blank=False,
        verbose_name=u"назва п*ятого дня")
    day5 = models.TextField(
        blank=True,
        verbose_name=u"опис п*ятого дня")

    def __unicode__(self):
        return u"%s %s" % (self.title_day5, self.day5)

class day6(models.Model):

    title_day6 = models.CharField(
        max_length=256,
        blank=False,
        verbose_name=u"назва шостого дня")
    day6 = models.TextField(
        blank=True,
        verbose_name=u"опис шостого дня")

    def __unicode__(self):
        return u"%s %s" % (self.title_day6, self.day6)

class day7(models.Model):

    title_day7 = models.CharField(
        max_length=256,
        blank=False,
        verbose_name=u"назва сьомого дня")
    day7 = models.TextField(
        blank=True,
        verbose_name=u"опис сьомого дня")

    def __unicode__(self):
        return u"%s %s" % (self.title_day7, self.day7)

class day8(models.Model):

    title_day8 = models.CharField(
        max_length=256,
        blank=False,
        verbose_name=u"назва восьмого дня")
    day8 = models.TextField(
        blank=True,
        verbose_name=u"опис восьмого дня")

    def __unicode__(self):
        return u"%s %s" % (self.title_day8, self.day8)

class User_Email(models.Model):

    class Meta(object):
        verbose_name = u"емейл користувача"
        verbose_name_plural = u"емейли користувачів"

    email = models.EmailField(
        max_length=200,
        blank=False,
        null=True,
        verbose_name=u'Ваш email')

    name = models.CharField(
        max_length=256,
        blank=False,
        null=True,
        verbose_name=u"Ваше ім'я")

    journey_choice = models.ForeignKey('Journey',
        verbose_name=u"Мандрівка",
        blank=True,
        null=True,
        on_delete=models.SET_NULL)


    def __unicode__(self):
        return u"%s %s %s" % (self.name, self.email, self.journey_choice)
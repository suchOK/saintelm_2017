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

    conditions = models.TextField(
        blank=True,
        verbose_name=u"умови")

    documents = models.TextField(
        blank=True,
        verbose_name=u"документи")

    options = models.TextField(
        blank=True,
        verbose_name=u"додаткові опції")


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
# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.core.urlresolvers import reverse
from django.db import models
from photologue.models import Gallery
from tinymce import models as tinymce_models

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

    slug = models.SlugField(max_length=100, unique=True)

    active = models.BooleanField(default=True)

    gallery = models.ForeignKey('photologue.Gallery',
        verbose_name=u"фотки",
        blank=True,
        null=True,
        related_name='gallery',
        on_delete=models.SET_NULL)

    describe = tinymce_models.HTMLField(
        blank=True,
        verbose_name=u"короткий опис")

    cities = tinymce_models.HTMLField(
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

    day = models.ManyToManyField('Day',
        blank=True,
        default='',
        verbose_name=u"опис мандрівного дня")

    conditions = tinymce_models.HTMLField(
        blank=True,
        verbose_name=u"умови")

    documents = tinymce_models.HTMLField(
        blank=True,
        verbose_name=u"документи")

    options = tinymce_models.HTMLField(
        blank=True,
        null=True,
        verbose_name=u"додаткові опції")

    price_include = tinymce_models.HTMLField(
        blank=True,
        null=True,
        verbose_name=u"у вартість входить")

    price_not_include = tinymce_models.HTMLField(
        blank=True,
        null=True,
        verbose_name=u"у вартість не входить")

    donation = tinymce_models.HTMLField(
        blank=True,
        null=True,
        verbose_name=u"пожертва")

    def get_absolute_url(self):
        return reverse("details", kwargs={"slug" : self.slug})

    def __str__(self):
        return u"%s" % (self.title)


class Day(models.Model):

    class Meta(object):
        verbose_name = u"День"
        verbose_name_plural = u"Дні"
        ordering = ['date_day']

    title_day = models.CharField(
        max_length=256,
        blank=False,
        verbose_name=u"назва дня")

    description = tinymce_models.HTMLField(
        blank=True,
        verbose_name=u"опис дня")

    date_day = models.DateField(verbose_name=u"дата дня")

    def __str__(self):
        return u"%s %s" % (self.title_day, self.description)



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
        verbose_name=u"Ваше ім'я та номер телефону")

    journey_choice = models.ForeignKey('Journey',
        verbose_name=u"Мандрівка",
        blank=True,
        null=True,
        on_delete=models.SET_NULL)

    def __str__(self):
        return u"%s %s %s" % (self.name, self.email, self.journey_choice)


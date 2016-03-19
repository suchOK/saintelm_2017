# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Post(models.Model):
    """Journey Model"""

    class Meta(object):
        verbose_name = u"Пост"
        verbose_name_plural = u"Пости"

    title = models.CharField(
        max_length=256,
        blank=False,
        verbose_name=u"назва поста")

    datetime = models.DateTimeField(u'Дата публікації')

    description = models.TextField(
        blank=True,
        verbose_name=u"короткий опис")

    text = models.TextField(
        blank=True,
        verbose_name=u"текст")

    blog_photo = models.ImageField(
        blank=True,
        verbose_name=u"фото",
        null=True)

    def __unicode__(self):
        return u"%s" % (self.title)

    def get_absolute_url(self):
    	return "/blog/%i/" % self.id
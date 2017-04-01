# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse
from tinymce import models as tinymce_models

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

    slug = models.SlugField(max_length=100, unique=True)

    datetime = models.DateTimeField(u'Дата публікації')

    description = tinymce_models.HTMLField(
        blank=True,
        verbose_name=u"короткий опис")

    text = tinymce_models.HTMLField(
        blank=True,
        verbose_name=u"текст")

    blog_photo = models.ImageField(
        blank=True,
        verbose_name=u"фото",
        null=True)

    def __str__(self):
        return u"%s" % (self.title)

    # def get_absolute_url(self):
    # 	return "/blog/%i/" % self.id

    def get_absolute_url(self):
        return reverse("posts", kwargs={"slug" : self.slug})
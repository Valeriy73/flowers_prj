from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Item(models.Model):
    """ Item Model """

    class Meta(object):
        verbose_name = u"Карточка товара"
        verbose_name_plural = u"Карточки товаров"

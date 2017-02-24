# -*- encoding: utf-8 -*- 
from __future__ import unicode_literals
from django.db import models


# Create your models here.
class Item(models.Model):
    """ Item Model """

    #class Meta(object):
    #    verbose_name = u"Карточка товара"
    #    verbose_name_plural = u"Карточки товаров"

    title = models.CharField(max_length=255, verbose_name='Название букета')
    description = models.TextField(verbose_name="Описание букета")
    price = models.IntegerField(default=0, verbose_name="Цена")
    image = models.TextField(verbose_name="Ссылка на изображение")

    def __str__(self):
        return 'Букет %s' % self.title


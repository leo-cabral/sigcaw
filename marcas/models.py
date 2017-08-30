# -*- coding: UTF-8 -*-
from django.db import models
from django.utils.translation import ugettext as _


class Marca(models.Model):
    nombre = models.CharField(
        max_length=255,
        verbose_name=_('Nombre de la marca'))

    def __str__(self):
        return "{0}".format(self.nombre)


class Modelo(models.Model):
    marca = models.ForeignKey(
        Marca,
        verbose_name=_("Nombre modelo"),
        related_name='modelo')
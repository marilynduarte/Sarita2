# -*- coding: utf-8 -*-

from django.db import models

class Persona(models.Model):
    nombre = models.CharField('nombre completo', max_length=50)
    direccion = models.CharField('direccion', max_length=80)
    telefono = models.CharField('telefono', max_length=8, null = True, blank = True)


    def __str__(self):
        return '%s' % (self.nombre)

    class Meta():
        abstract = True
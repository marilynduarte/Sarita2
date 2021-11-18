# -*- coding: utf-8 -*-
from django.db import models
from comun.models import Persona
from django.utils.safestring import mark_safe
from compra import *


class Proveedor(Persona):
    
    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'proveedor'
        verbose_name = 'Proveedor'
        verbose_name_plural = 'Proveedores'


class Categoria(models.Model):

    descripcion = models.CharField('Nombre de la categoria', max_length=50)
   #definir unidad de medida para insumos(unidades), para cubeta de helado(onza o gramo), paleteria (undidades)

    def __str__(self):
        return self.descripcion

    class Meta:
        db_table = 'categoria'
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'


class Producto(models.Model):

    categoria = models.ForeignKey(Categoria,
        on_delete=models.CASCADE,null=False)
    nombre = models.CharField('Nombre del producto',
        max_length=50,null=False)
    precio_venta = models.DecimalField('Precio de Venta',
        max_digits=7, decimal_places=2, null=False)
    existencia = models.PositiveIntegerField('Existencia',
        null=False, default=0)

    def __str__(self):
        try:
            return '%s %s' %(self.nombre, self.existencia)
        except:
            return self.nombre


    class Meta:
        db_table = 'producto'
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'


class DetalleProducto(models.Model):
    producto=models.ForeignKey(Producto, on_delete=models.CASCADE,
        null=False)
    lote=models.CharField('Numero de lote del producto',
        null=False, blank=False, max_length=50)
    subexistencias=models.PositiveIntegerField('Existencia',
        null=False, default=0)
    fechavencimiento=models.DateField('Fecha de vencimiento',
        null=True, blank=True)

    class Meta:
        db_table = 'detalleproducto'
        verbose_name = 'Detalle de Producto'
        verbose_name_plural = 'Detalle de Productos'


class Lote (models.Model):
    lote = models.CharField('Numero de lote del producto', null=False, blank=False, max_length=50)
    fechavencimiento = models.DateField('Fecha de vencimiento', null=True, blank=True)

    def __str__(self):
        return self.lote


    class Meta:
        db_table = 'lote'
        verbose_name = 'Lote'
        verbose_name_plural = 'Lotes'
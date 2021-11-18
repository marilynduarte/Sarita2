from django.db import models
from administracion.models import *
from datetime import date
from django.utils.safestring import mark_safe
#from django.shortcuts import render
from .models import *
from django.core.exceptions import ValidationError





class Compra(models.Model):

    fecha= models.DateField('Fecha de emisión',
        default=date.today,null=False, blank=False)
    seriefactura= models.CharField('Numero de Serie',
        null=False, blank=False, max_length=50)
    dtefactura= models.PositiveIntegerField('Numero de DTE',
        null=False, blank=False, default=None)
    proveedor=models.ForeignKey(Proveedor,
        on_delete=models.CASCADE, null=False)
    total=models.DecimalField('Total', max_digits=7,
        decimal_places=2, default=0.00)

    def compr(self):
        return mark_safe(
            u'<center><a href="/compra/?id=%s" target="_blank">Compra</a></center>' % self.id)

    def clean(self):
        if DetalleProducto.producto == None:
            raise ValidationError('Ingrese detalle de compra')
        if self.fecha > date.today():
            raise ValidationError ('No puede ingresar una fecha que aun no ha llegado')


    class Meta():   
        db_table = 'compra'
        verbose_name = 'Compra'
        verbose_name_plural = 'Compras'


class DetalleCompra(models.Model):

    compra=models.ForeignKey(Compra, 
        on_delete=models.CASCADE)
    producto= models.ForeignKey(Producto, 
        on_delete=models.CASCADE, null=False)
    fechavencimiento = models.DateField('Fecha de vencimiento', 
        null=False, blank=False)
    lote = models.CharField('Numero de lote del producto', 
        null=False, blank=False, max_length=50)
    cantidad = models.PositiveIntegerField('Cantidad', 
        null=False, default=0)
    precio_compra=models.DecimalField('Precio de compra', 
        max_digits=7, decimal_places=2)
    subtotal = models.PositiveIntegerField('subtotal', 
        null=False, blank=False, default=0.00)


    def compr(self):
        return mark_safe(
            u'<center><a href="/detallecompra/?id=%s" target="_blank">Detallecompra</a></center>' % self.id)

    class Meta():
        db_table = 'detalle_compra'
        verbose_name = 'Detalle de Compra'
        verbose_name_plural = 'Detalle de Compras'



    def clean(self):
        if self.fechavencimiento == None:
            raise ValidationError ('Ingrese fecha de vencimiento')
        if self.fechavencimiento <= date.today():
            raise ValidationError ('La fecha ingresada ya expiró o expirará hoy. Verificar nuevamente la fecha de vencimiento') 

        newdetalleproducto= DetalleProducto.objects.filter(
            lote = self.lote).all()

        for e in newdetalleproducto:
            if e.lote == self.lote:
                if e.fechavencimiento != self.fechavencimiento:
                    raise ValidationError ('La fecha de vencimiento del lote '
                        + str(e.lote) + ' es ' + str(e.fechavencimiento))


#Métodos del Sistema SARISYS
    def save (self, force_insert=False, force_update=False, using=None):


        detalleproducto= DetalleProducto.objects.filter(producto = self.producto).all()
        newdetalleproducto= DetalleProducto.objects.filter(lote = self.lote).all()

        if detalleproducto == None:
            detalleproducto= DetalleProducto.objects.create(producto = self.producto, lote = self.lote, subexistencias = self.cantidad, fechavencimiento = self.fechavencimiento)
        else:

            mp = DetalleCompra.objects.filter(producto = self.producto).filter(lote = self.lote).first()
        
            if mp == None:

                detalleproducto= DetalleProducto.objects.create(producto = self.producto, lote = self.lote, subexistencias = self.cantidad, fechavencimiento = self.fechavencimiento)

            else:

                for e in newdetalleproducto:
                    if e.lote == self.lote:

                        if e.fechavencimiento != self.fechavencimiento:
                            raise ValidationError ('La fecha de vencimiento del lote ' + str(e.lote) + ' es ' + str(e.fechavencimiento))
                        else:
                            e.subexistencias += self.cantidad
                            print ("esta es una prueba de existencias")
                            e.save()





        # metodo para la operación del subtotal
        self.subtotal = (self.cantidad * self.precio_compra)

        # metodo para sumar el total de la compra
        totalcompra = Compra.objects.all().last()
        totalcompra.total = (totalcompra.total + self.subtotal)
        totalcompra.save()


        sumatotalproducto= Producto.objects.filter(id = 
            self.producto.id).first()
        sumatotalproducto.existencia = 0
        for j in sumatotalproducto.detalleproducto_set.filter(
            producto__id = sumatotalproducto.id):
            sumatotalproducto.existencia += j.subexistencias
            sumatotalproducto.save()
        


        lote = Lote.objects.filter(lote = self.lote).first()
        fechavencimiento = Lote.objects.filter(fechavencimiento = self.fechavencimiento).first()
        if lote == None:
            lote= Lote.objects.create(lote = self.lote, fechavencimiento = self.fechavencimiento)
            

        super(DetalleCompra, self).save(force_insert, force_update, using)

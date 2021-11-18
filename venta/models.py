from django.db import models
from datetime import date
from django.db import transaction
from django.core.exceptions import ValidationError
from django.utils.safestring import mark_safe
from compra.models import *
from administracion.models import *
from reportlab.pdfgen import canvas
from django.http import HttpResponse
from django.conf import settings
from django.db import models
from django.contrib.auth.models import User, BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import User



class Venta(models.Model):

    fecha = models.DateField('fecha', default=date.today,
        null=False, blank=False)
    vendedor= models.ForeignKey(User, on_delete=models.CASCADE, 
        null=True, blank=True)
    total = models.FloatField('total', null=True, blank=True, 
        default=0.00)
    efectivo = models.FloatField('efectivo', null=True, 
        blank=True, default=0.00)
    vuelto = models.FloatField('vuelto', null=True, 
        blank=True, default=0.00)
    

    def save (self, force_insert=False, force_update=False, using=None):

        self.vuelto = (self.efectivo - self.total)

        super(Venta, self).save(force_insert, force_update, using)


    class Meta:
        db_table = 'venta'
        verbose_name = 'Venta'
        verbose_name_plural = 'Ventas'



class DetalleVenta(models.Model):

    venta = models.ForeignKey(Venta, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    lote = models.CharField('Numero de lote', null=False, 
        blank=False, max_length=50)
    cantidad = models.PositiveIntegerField('cantidad')
    subtotal = models.FloatField('subtotal', null=True, 
        blank=True, default=0.00)


    def clean(self):
        if lote == None:
            raise ValidationError ('Ingrese Lote')

    class Meta:
        db_table = 'detalle_venta'
        verbose_name = 'Detalle de Venta '
        verbose_name_plural = 'Detalles de Ventas'



# Funciones que realizan validaciones


    def clean(self):
        #Hace un filtro del producto y el lote
        mp = DetalleCompra.objects.filter(
            producto = self.producto).filter(
            lote = self.lote).first()

        detalleproducto= DetalleProducto.objects.filter(
            producto = self.producto).all()

        if mp == None:
            raise ValidationError('No existe el Lote ') #Validación cuando el lote ingresado no existe
        if mp.lote==self.lote: #Si el lote el igual al que el usuario selecciono, continue a la siguiente validación
            for e in detalleproducto:
                if e.lote == self.lote:
                    if mp.fechavencimiento <= date.today():#Si la fecha es mejor al dia de hoy, miestre el siguiente mensaje
                        raise ValidationError('El producto de este lote ya esta vencido')
                    if e.subexistencias >= self.cantidad:
                        e.subexistencias -= self.cantidad
                        e.save()
                    else:
                        raise ValidationError('Sin existencias en este lote')


#Fuciones para calcular el total, subtotal y disminuir las existencias
    def save (self, force_insert=False, force_update=False, using=None):

        # metodo para la operación del subtotal
        self.subtotal = float(self.cantidad * self.producto.precio_venta)

       

        sumatotalproducto= Producto.objects.filter(id = self.producto.id).first()
        sumatotalproducto.existencia = 0
        for j in sumatotalproducto.detalleproducto_set.filter(producto__id = sumatotalproducto.id):
            sumatotalproducto.existencia += j.subexistencias
            sumatotalproducto.save()

        venta = Venta.objects.all().last()
        venta.total = float(venta.total + self.subtotal)
        venta.save()
                   


        super(DetalleVenta, self).save(force_insert, force_update, using)

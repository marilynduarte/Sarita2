from django.db import models
from compra.models import *
from venta.models import *
from administracion.models import *
from django.utils.safestring import mark_safe
from datetime import datetime
from django.core.exceptions import ValidationError


TIPO_INFORME =(
    ('Compra', 'Compra'),
    ('Venta', 'Venta'),
)#Choice para seleccionar tipo de de informe

INFORME_GENERAL =(
    ('Existencias', 'Existencias'),
    ('Lotes', 'Lotes')
   
)#Choice para seleccionar tipo de de informe

#Informe -----------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
class InformePorRango(models.Model):
    tipo_dev=models.CharField('Tipo de Informe', max_length=15,
        choices=TIPO_INFORME, default= 'Compra')
    fecha_inicio = models.DateField('Fecha De Inicio')
    fecha_limite = models.DateField('Fecha De Limite')
    total_compras = models.DecimalField('Total de Compras',max_digits=7,
        decimal_places=2, null=False, default=0.00)
    total_ventas = models.DecimalField('Total Ventas',max_digits=7,
        decimal_places=2, null=False, default=0.00)
    


    def generar_informe(self):
            return mark_safe('<a target="_blank" href="/informe/'+str(self.id)+'"class="informe">Imprimir</a>')


    def clean(self):
        super(InformePorRango, self).clean()
        if (self.fecha_limite > datetime.now().date() ):
            raise ValidationError('No Puede obtener datos de una fecha a futuro')


    def save (self, force_insert=False, force_update=False, using=None):

        self.total_compras=0
        self.total_ventas=0

        for e in Compra.objects.all():
            if (e.fecha >= self.fecha_inicio
                and e.fecha <= self.fecha_limite):
                self.total_compras+=e.total
                        
        for i in Venta.objects.all():
            if (i.fecha >= self.fecha_inicio
                and i.fecha <= self.fecha_limite):
                self.total_ventas+=i.total


        super(InformePorRango, self).save(force_insert, force_update, using)


    class Meta():
        db_table = 'informe_por_rango'
        verbose_name = 'Informe por Rango'
        verbose_name_plural = 'Informe por Rangos'


class InformePorLote(models.Model):

    tipo_lote=models.ForeignKey(Lote, on_delete=models.CASCADE)


    def generar_informe(self):
            return mark_safe('<a target="_blank" href="/informelotes/'+str(self.id)+'"class="informelotes">Imprimir</a>')


    class Meta():
        db_table = 'informe_por_lote'
        verbose_name = 'Informe por Lote'
        verbose_name_plural = 'Informe por Lotes'




class InformeGeneral(models.Model):

    info_grl=models.CharField('Tipo de Informe', max_length=15,
        choices=INFORME_GENERAL, default= 'Existencias')
    exist = models.PositiveIntegerField('Existencias', null=False,
        default=0)

    def __str__(self):
        return self.info_grl

 
    def generar_informe(self):
            return mark_safe('<a target="_blank" href="/informegeneral/'+str(self.id)+'"class="informegeneral">Imprimir</a>')


    class Meta():
        db_table = 'informe_general'
        verbose_name = 'Informe General'
        verbose_name_plural = 'Informes Generales'

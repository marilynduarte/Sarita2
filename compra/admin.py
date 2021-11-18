from django.contrib import admin
from .models import *


class DetCompraInline(admin.TabularInline):
	model = DetalleCompra	
	extra = 1

	fields = [
			
					'compra',
					'producto', 
					'fechavencimiento',
					'lote',
					'cantidad',
					'precio_compra',
					'subtotal'
				]

	autocomplete_fields = ['producto']
	readonly_fields = ['subtotal']
	#autocompletar 
	


class CompraAdmin(admin.ModelAdmin):
    inlines = [DetCompraInline]
    readonly_fields = ['total']
    #search_fields = ['proveedor']
    list_filter = ['proveedor', 'fecha']
    list_display = ['fecha', 'seriefactura','dtefactura', 'proveedor','total']



admin.site.register(Compra,CompraAdmin)
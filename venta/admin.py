from django.contrib import admin
from django.contrib.auth.models import User
from .models import *



 
class DetVentaInline(admin.TabularInline):
	model = DetalleVenta	
	extra = 1

	readonly_fields = ['subtotal']



class VentaAdmin(admin.ModelAdmin):
	readonly_fields = ['fecha','total','vendedor','vuelto']
	inlines = [DetVentaInline]
	#readonly_fields = ['fecha','total','vuelto']
	list_display = ['fecha','total']


	def save_model(self, request, obj, form, change):#capturar quien crea la publicación
		if getattr(obj, 'vendedor', None) is None:
			obj.vendedor = request.user
			obj.save()



admin.site.register(Venta,VentaAdmin)

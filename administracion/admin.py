from django.contrib import admin
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


class UserAdmin(BaseUserAdmin):#Sobre escribe el modelo administrativo de usuario
	readonly_fields = ['is_superuser', 'user_permissions']
	list_per_page = 12
	

admin.site.unregister(User)
admin.site.register(User, UserAdmin)


class ProveedorAdmin(admin.ModelAdmin):
   
	search_fields = ['nombre']
	list_filter = ['direccion']
	list_display = ['nombre', 'direccion', 'telefono']

class CategoriaAdmin(admin.ModelAdmin):
    
	search_fields = ['descripcion']
	list_filter = ['descripcion']
	list_display = ['descripcion']
   

class DetProductoInline(admin.TabularInline):
	model = DetalleProducto	
	extra = 1

	readonly_fields= ['producto','lote','subexistencias','fechavencimiento']
	list_filter = ['lote']
	list_display = ['producto', 'lote', 'subexistencias','fechavencimiento']


class ProductoAdmin(admin.ModelAdmin):

	inlines = [DetProductoInline]
	search_fields = ['nombre']
	list_filter = ['categoria']
	list_display = ['nombre',  'categoria','precio_venta','existencia']
    #raw_id_fields=['proveedor']
	autocomplete_fields=['categoria']
	readonly_fields = ['existencia',]
	



class InformeAdmin(admin.ModelAdmin):
	list_display = ['informe']


admin.site.register(Proveedor, ProveedorAdmin)
admin.site.register(Categoria,CategoriaAdmin)
admin.site.register(Producto, ProductoAdmin)


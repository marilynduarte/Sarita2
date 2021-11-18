from django.contrib import admin
from .models import *


class InformePorRangoAdmin(admin.ModelAdmin):
	
	fields = [
			
					'fecha_inicio',
					'fecha_limite', 
					'tipo_dev',
				]


	list_display = ['tipo_dev','fecha_inicio', 'fecha_limite','generar_informe']






class InformePorLoteAdmin(admin.ModelAdmin):
	
	fields = [
			
					'tipo_lote',
				]


	list_display = ['tipo_lote','generar_informe']






class InformeGeneralAdmin(admin.ModelAdmin):
	
	fields = [
			 
					'info_grl',
				]


	list_display = ['info_grl','generar_informe']



admin.site.register(InformePorLote,InformePorLoteAdmin)
admin.site.register(InformePorRango,InformePorRangoAdmin)
admin.site.register(InformeGeneral,InformeGeneralAdmin)



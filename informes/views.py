from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
import os
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect
from django.template import Context
from django.template.loader import get_template
from xhtml2pdf import pisa
from datetime import datetime
from .models import *
from compra.models import *
from venta.models import *
from informes.models import *
from administracion.models import *



class ComprasYVentasPDF(View):#PDF para la constancia de Estudios

	def link_callback(self, uri, rel):
		sUrl = settings.STATIC_URL # Typically /static/
		sRoot = settings.STATIC_ROOT # Typically /home/userX/project_static/
		mUrl = settings.MEDIA_URL # Typically /static/media/
		mRoot = settings.MEDIA_ROOT # Typically /home/userX/project_static/media/

        # convert URIs to absolute system paths
		if uri.startswith(mUrl):
			path = os.path.join(mRoot, uri.replace(mUrl, ""))
		elif uri.startswith(sUrl):
			path = os.path.join(sRoot, uri.replace(sUrl, ""))
		else:
			return uri # handle absolute uri (ie: http://some.tld/foo.png)

        # make sure that file exists
		if not os.path.isfile(path):
			raise Exception(
				'media URI must start with %s or %s' % (sUrl, mUrl)
			)
		return path


	def get(self, request, *args, **kwargs):
	
		template = get_template('home/InformeComprasVentas.html')#define la ruta del html a ser pdf
		context = {
			'compras': Compra.objects.all(),#accede a los datos de la base, con pk=self.kwargs['pk'] acede al id que le enviamos
			'ventas': Venta.objects.all(),#accede a los datos de la base, con pk=self.kwargs['pk'] acede al id que le enviamos
			'existencias': Producto.objects.all(),#accede a los datos de la base, con pk=self.kwargs['pk'] acede al id que le enviamos
			'rango': InformePorRango.objects.get(pk=self.kwargs['pk']),#accede a los datos de la base, con pk=self.kwargs['pk'] acede al id que le enviamos
			'iconsarita': '{}{}'.format(settings.MEDIA_URL, 'logo_sarita.png'),
			
			'fecha': datetime.now().date()
		}#dixionario de datos
		html = template.render(context)#manda el dixionario de datos
		response = HttpResponse(content_type='application/pdf')
		#response['Content-Disposition'] = 'attachment; filename="cosntancia.pdf"'
		pisaStatus = pisa.CreatePDF(

			html, dest=response,#crea el html
			link_callback=self.link_callback)#llama la imagen

		return response




class InformePorLotesPDF(View):#PDF para informe por lotes

	def link_callback(self, uri, rel):
		sUrl = settings.STATIC_URL # Typically /static/
		sRoot = settings.STATIC_ROOT # Typically /home/userX/project_static/
		mUrl = settings.MEDIA_URL # Typically /static/media/
		mRoot = settings.MEDIA_ROOT # Typically /home/userX/project_static/media/

        # convert URIs to absolute system paths
		if uri.startswith(mUrl):
			path = os.path.join(mRoot, uri.replace(mUrl, ""))
		elif uri.startswith(sUrl):
			path = os.path.join(sRoot, uri.replace(sUrl, ""))
		else:
			return uri # handle absolute uri (ie: http://some.tld/foo.png)

        # make sure that file exists
		if not os.path.isfile(path):
			raise Exception(
				'media URI must start with %s or %s' % (sUrl, mUrl)
			)
		return path


	def get(self, request, *args, **kwargs):


		template2 = get_template('home/informeporlotes.html')
		context2 = {

			'iconsarita': '{}{}'.format(settings.MEDIA_URL, 'logo_sarita.png'),
			'lote': InformePorLote.objects.get(pk=self.kwargs['pk']),
			'detallelote':DetalleProducto.objects.all(),
			'producto':Producto.objects.all(),
			'fecha': datetime.now().date()
		}
		html = template2.render(context2)
		response = HttpResponse(content_type='application/pdf')
		pisaStatus = pisa.CreatePDF(

			html, dest=response,#crea el html
			link_callback=self.link_callback)#llama la imagen

		return response





class InformeGeneralPDF(View):#PDF para la constancia de Estudios

	def link_callback(self, uri, rel):
		sUrl = settings.STATIC_URL # Typically /static/
		sRoot = settings.STATIC_ROOT # Typically /home/userX/project_static/
		mUrl = settings.MEDIA_URL # Typically /static/media/
		mRoot = settings.MEDIA_ROOT # Typically /home/userX/project_static/media/

        # convert URIs to absolute system paths
		if uri.startswith(mUrl):
			path = os.path.join(mRoot, uri.replace(mUrl, ""))
		elif uri.startswith(sUrl):
			path = os.path.join(sRoot, uri.replace(sUrl, ""))
		else:
			return uri # handle absolute uri (ie: http://some.tld/foo.png)

        # make sure that file exists
		if not os.path.isfile(path):
			raise Exception(
				'media URI must start with %s or %s' % (sUrl, mUrl)
			)
		return path


	def get(self, request, *args, **kwargs):
	
		template = get_template('home/existencias.html')#define la ruta del html a ser pdf
		context = {
			'existencias': Producto.objects.all(),#accede a los datos de la base, con pk=self.kwargs['pk'] acede al id que le enviamos
			'iconsarita': '{}{}'.format(settings.MEDIA_URL, 'logo_sarita.png'),
			'fecha': datetime.now().date(),
			'general': InformeGeneral.objects.get(pk=self.kwargs['pk']),#accede a los datos de la base, con pk=self.kwargs['pk'] acede al id que le enviamos
		}#dixionario de datos
		html = template.render(context)#manda el dixionario de datos
		response = HttpResponse(content_type='application/pdf')
		#response['Content-Disposition'] = 'attachment; filename="cosntancia.pdf"'
		pisaStatus = pisa.CreatePDF(

			html, dest=response,#crea el html
			link_callback=self.link_callback)#llama la imagen

		return response




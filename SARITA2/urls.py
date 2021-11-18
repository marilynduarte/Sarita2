"""SARITA2 URL Configuration    

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from administracion.views import *
from compra.views import *
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from informes.views import *
from django.contrib.auth.decorators import login_required #para que sea login


urlpatterns = [
    path('', admin.site.urls),
    #path ('home/productos',InformePDF.as_view(),name= 'informe')
    #path('pedido', InformeDeCompra.as_view(), name= 'mi_pdf'),
    #path('detallepedido', InformeDetalladoCompra.as_view(), name= 'mi_pdf'),
    path('informe/<int:pk>', login_required(ComprasYVentasPDF.as_view()), name='informe'),
    path('informelotes/<int:pk>', login_required(InformePorLotesPDF.as_view()), name='informelotes'),
    path('informegeneral/<int:pk>', login_required(InformeGeneralPDF.as_view()), name='informegeneral'),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.contrib import admin
from django.urls import path
from . import views

app_name = "producto_app"

urlpatterns = [
    path(
    	'Lista/', 
    	views.ListaProductosListView.as_view(),
    	name='Lista'

]

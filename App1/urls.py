
from django.urls import path
from .views import *


urlpatterns = [
   path('', inicio, name='Inicio'),
   path('agregar/', agregar, name='Agregar'),
   path('buscar/', buscarCafeterias, name='Buscar'),
   path('valoranos/', valoranos, name='Valoranos'),
   path('suscribite/', suscribirse, name='Suscribirse'),
   path('leerCafeterias', leerCafeterias, name = "LeerCafeterias")
]

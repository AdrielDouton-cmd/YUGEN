from django.urls import path
from .views import *

urlpatterns = [

    path('', inicio),
    path('carta', carta),
    path('locales', locales),
    path('reserva', reserva, name='reservaS'),
    path('registrarse/', crear_registro, name='crear_cliente'),
    path('eventos/', crear_evento, name='crear_evento'),
    path('busqueda-evento/', busqueda_evento, name='busqueda_evento'),
    path('buscar/', buscar_evento, name= 'buscar_evento'),
    path('busqueda-cliente/', busqueda_cliente, name='busqueda_cliente'),
    path('buscar-cliente/', buscar_cliente, name= 'buscar_cliente'),

]

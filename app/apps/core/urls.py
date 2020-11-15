from django.conf.urls import url
from .views import *

urlpatterns=[
    url(r'^$',home,name="index"),
    url(r'^crear_producto/',crearproducto,name="crear_producto"),
    url(r'^listar_producto/',listarproducto,name="listar_producto"),
]
from django.test import TestCase
from config.wsgi import *
from core.erp.models import Type,Employee
# Create your tests here.

#esta es la forma de un select * from tabla
query=Type.objects.all()
print(query)

#esta es la forma de una insercion insert into
#t=Type(names='Administrador').save()
#t.names='programador'
#t.save()

#edicion o update
#try:
    #t=Type.objects.get(id=2)
    #t.names='Programador'
    #t.save()
#except Exception as e:
    #print(e)

#eliminacion
#t=Type.objects.get(id=3)
#t.delete()

#toma en cuenta si es mayuscula
#obj=Type.objects.filter(names__contains="Pro")

#no toma en cuenta si es mayuscula
#obj=Type.objects.filter(names__icontains="pro")


#contar cuantos registros
#obj=Type.objects.filter(names__in=["Analista"]).count()

#desplegar la consulta sql que se hace
#obj=Type.objects.filter(names__icontains="pro").query

obj=Employee.objects.filter(type__id=1)

#obj=Type.objects.filter(names__icontains="Pro").exclude(id=1)
print(obj)
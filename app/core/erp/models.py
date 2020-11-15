from django.db import models
from datetime import datetime

from django.db.models import CharField
from django.forms import model_to_dict

from core.erp.choices import gender_choices


#class Category(models.Model):
 #   name = models.CharField(max_length=150, verbose_name='Nombre', unique=True)
  #  desc: CharField = models.CharField(max_length=500, null=True, blank=True, verbose_name='Descripción')

   # def __str__(self):
    #    return self.name

   # class Meta:
    #    verbose_name = 'Categoria'
    #    verbose_name_plural = 'Categorias'
    #    ordering = ['id']


class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name='Nombre', unique=True)
    descripcion = models.CharField(max_length=150, verbose_name='Descripcion')
    pcompra = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    pventa = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)

    def __str__(self):
        return self.name

    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        ordering = ['id']

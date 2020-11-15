from django.db import models

class Product(models.Model):
    id=models.AutoField(primary_key=True)
    name = models.CharField(max_length=150, verbose_name='Nombre', unique=True)
    categoria = models.CharField(max_length=100, verbose_name='Categoría')
    pcompra = models.DecimalField(default=0.00, max_digits=9, decimal_places=2, verbose_name='Precio de compra')
    pventa = models.DecimalField(default=0.00, max_digits=9, decimal_places=2, verbose_name='Precio de venta')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        ordering = ['id']

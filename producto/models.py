from django.db import models
from negocio.models import Negocio
# Create your models here.
class Producto(models.Model):
    id = models.AutoField(primary_key=True,verbose_name=("id"))
    negocio_id = models.ForeignKey(Negocio, on_delete = models.CASCADE,verbose_name=("Negocio"))
    nombre = models.CharField(max_length=250, blank=True,verbose_name=("Nombre"))
    descripcion = models.CharField(max_length=250, blank=True,verbose_name=("Descripción"))
    imagen = models.ImageField(blank=True,verbose_name=("Imagen"))
    cantidad = models.IntegerField(verbose_name=("Cantidad"))
    precio = models.FloatField(verbose_name=("Precio"))

    class Meta:
        verbose_name = ('Producto')
        verbose_name_plural = ('Productos')

    def __str__(self):
        return self.nombre
from django.contrib import admin
from django.db import models

# Create your models here.
class Negocio(models.Model):
    id = models.AutoField(primary_key=True)
    ruc = models.CharField(max_length=250)
    nombre = models.CharField(max_length=250, blank=True)
    descripcion = models.CharField(max_length=250, blank=True)
    imagen = models.ImageField(blank=True)

    class Meta:
        verbose_name = ('Negocio')
        verbose_name_plural = ('Negocios')

    def __str__(self):
        return self.nombre
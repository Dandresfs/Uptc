from django.db import models
from inventario_equipos.models import InventarioEquipos

class TipoMantenimiento(models.Model):
    nombre = models.CharField('Tipo mantenimiento',max_length=100)

    def __str__(self):
        return self.nombre

class Actividades(models.Model):
    maquina = models.ForeignKey(InventarioEquipos)
    tipo = models.ForeignKey(TipoMantenimiento)
    nombre = models.CharField('Codigo actividad',max_length=100)
    descripcion = models.TextField('Descripcion',max_length=200)
    imagen = models.ImageField('Imagen', upload_to='Actividades/Imagenes/')

    def __str__(self):
        return self.nombre



class EventCalendar(models.Model):
    title = models.CharField('Titulo',max_length=100)
    start = models.CharField('Inicio',max_length=100)
    end = models.CharField('Fin',max_length=100,blank=True, null=True)
    color = models.CharField('Color',max_length=100,blank=True,null=True)
    icono = models.CharField('Icono',max_length=100,blank=True,null=True)
    mantenimiento = models.ForeignKey(TipoMantenimiento)
    maquina = models.ForeignKey(InventarioEquipos)

    def __str__(self):
        return self.title
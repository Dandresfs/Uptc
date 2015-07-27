from django.db import models

class InventarioEquipos(models.Model):
    nombre = models.CharField('Nombre Maquina',max_length=100)
    descripcion = models.TextField('Descripcion',max_length=200)
    color = models.CharField('Color',max_length=100)
    imagen = models.ImageField('Imagen', upload_to='Inventario de Equipos/Imagenes/')
    pdf = models.FileField(upload_to='Inventario de Equipos/')

    def __str__(self):
        return self.nombre

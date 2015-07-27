from django.db import models

class InventarioEquipos(models.Model):
    nombre = models.CharField('Nombre Maquina',max_length=100)
    descripcion = models.TextField('Descripcion',max_length=200)
    color = models.CharField('Color',max_length=100)
    imagen = models.ImageField('Imagen', upload_to='Inventario de Equipos/Imagenes/')
    preventivo = models.FileField('Plan Preventivo', upload_to='Planes/Preventivo/',blank=True)
    correctivo = models.FileField('Plan Correctivo', upload_to='Planes/Correctivo/',blank=True)
    predictivo = models.FileField('Plan Predictivo', upload_to='Planes/Predictivo/',blank=True)
    rcm = models.FileField('Plan Rcm', upload_to='Planes/Rcm/',blank=True)
    tpm = models.FileField('Plan Tpm', upload_to='Planes/Tpm/',blank=True)
    pdf = models.FileField(upload_to='Inventario de Equipos/')

    def __str__(self):
        return self.nombre

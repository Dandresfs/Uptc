# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='InventarioEquipos',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre Maquina')),
                ('descripcion', models.TextField(max_length=200, verbose_name='Descripcion')),
                ('color', models.CharField(max_length=100, verbose_name='Color')),
                ('imagen', models.ImageField(verbose_name='Imagen', upload_to='Inventario de Equipos/Imagenes/')),
                ('pdf', models.FileField(upload_to='Inventario de Equipos/')),
            ],
        ),
    ]

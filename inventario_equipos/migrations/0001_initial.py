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
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(verbose_name='Nombre Maquina', max_length=100)),
                ('descripcion', models.TextField(verbose_name='Descripcion', max_length=200)),
                ('imagen', models.ImageField(upload_to='Inventario de Equipos/Imagenes/', verbose_name='Imagen')),
                ('pdf', models.FileField(upload_to='Inventario de Equipos/')),
            ],
        ),
    ]

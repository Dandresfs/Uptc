# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventario_equipos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Actividades',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=100, verbose_name='Codigo actividad')),
                ('descripcion', models.TextField(max_length=200, verbose_name='Descripcion')),
                ('maquina', models.ForeignKey(to='inventario_equipos.InventarioEquipos')),
            ],
        ),
    ]

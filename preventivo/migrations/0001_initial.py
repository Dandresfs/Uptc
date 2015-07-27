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
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('nombre', models.CharField(max_length=100, verbose_name='Codigo actividad')),
                ('descripcion', models.TextField(max_length=200, verbose_name='Descripcion')),
                ('imagen', models.ImageField(verbose_name='Imagen', upload_to='Actividades/Imagenes/')),
                ('maquina', models.ForeignKey(to='inventario_equipos.InventarioEquipos')),
            ],
        ),
        migrations.CreateModel(
            name='EventCalendar',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('title', models.CharField(max_length=100, verbose_name='Titulo')),
                ('start', models.CharField(max_length=100, verbose_name='Inicio')),
                ('end', models.CharField(max_length=100, verbose_name='Fin', blank=True, null=True)),
                ('color', models.CharField(max_length=100, verbose_name='Color', blank=True, null=True)),
                ('icono', models.CharField(max_length=100, verbose_name='Icono', blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TipoMantenimiento',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('nombre', models.CharField(max_length=100, verbose_name='Tipo mantenimiento')),
            ],
        ),
        migrations.AddField(
            model_name='eventcalendar',
            name='mantenimiento',
            field=models.ForeignKey(to='preventivo.TipoMantenimiento'),
        ),
        migrations.AddField(
            model_name='eventcalendar',
            name='maquina',
            field=models.ForeignKey(to='inventario_equipos.InventarioEquipos'),
        ),
        migrations.AddField(
            model_name='actividades',
            name='tipo',
            field=models.ForeignKey(to='preventivo.TipoMantenimiento'),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventario_equipos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='inventarioequipos',
            name='correctivo',
            field=models.FileField(verbose_name='Plan Preventivo', upload_to='Inventario de Equipos/Correctivo/', blank=True),
        ),
        migrations.AddField(
            model_name='inventarioequipos',
            name='predictivo',
            field=models.FileField(verbose_name='Plan Preventivo', upload_to='Inventario de Equipos/Predictivo/', blank=True),
        ),
        migrations.AddField(
            model_name='inventarioequipos',
            name='preventivo',
            field=models.FileField(verbose_name='Plan Preventivo', upload_to='Inventario de Equipos/Preventivo/', blank=True),
        ),
        migrations.AddField(
            model_name='inventarioequipos',
            name='rcm',
            field=models.FileField(verbose_name='Plan Preventivo', upload_to='Inventario de Equipos/Rcm/', blank=True),
        ),
        migrations.AddField(
            model_name='inventarioequipos',
            name='tpm',
            field=models.FileField(verbose_name='Plan Preventivo', upload_to='Inventario de Equipos/Tpm/', blank=True),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventario_equipos', '0002_auto_20150727_1515'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventarioequipos',
            name='correctivo',
            field=models.FileField(upload_to='Planes/Correctivo/', verbose_name='Plan Correctivo', blank=True),
        ),
        migrations.AlterField(
            model_name='inventarioequipos',
            name='predictivo',
            field=models.FileField(upload_to='Planes/Predictivo/', verbose_name='Plan Predictivo', blank=True),
        ),
        migrations.AlterField(
            model_name='inventarioequipos',
            name='preventivo',
            field=models.FileField(upload_to='Planes/Preventivo/', verbose_name='Plan Preventivo', blank=True),
        ),
        migrations.AlterField(
            model_name='inventarioequipos',
            name='rcm',
            field=models.FileField(upload_to='Planes/Rcm/', verbose_name='Plan Rcm', blank=True),
        ),
        migrations.AlterField(
            model_name='inventarioequipos',
            name='tpm',
            field=models.FileField(upload_to='Planes/Tpm/', verbose_name='Plan Tpm', blank=True),
        ),
    ]

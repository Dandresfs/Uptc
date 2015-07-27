# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('preventivo', '0006_eventcalendar_icono'),
    ]

    operations = [
        migrations.AddField(
            model_name='actividades',
            name='imagen',
            field=models.ImageField(default='', upload_to='Actividades/Imagenes/', verbose_name='Imagen'),
            preserve_default=False,
        ),
    ]

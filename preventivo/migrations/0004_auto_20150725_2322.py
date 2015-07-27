# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventario_equipos', '0002_inventarioequipos_color'),
        ('preventivo', '0003_auto_20150725_1810'),
    ]

    operations = [
        migrations.CreateModel(
            name='TipoMantenimiento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(verbose_name='Tipo mantenimiento', max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='eventcalendar',
            name='maquina',
            field=models.ForeignKey(default='', to='inventario_equipos.InventarioEquipos'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='eventcalendar',
            name='mantenimiento',
            field=models.ForeignKey(default='', to='preventivo.TipoMantenimiento'),
            preserve_default=False,
        ),
    ]

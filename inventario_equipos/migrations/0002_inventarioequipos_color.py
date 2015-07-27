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
            name='color',
            field=models.CharField(default='#ff0000', max_length=100, verbose_name='Color'),
            preserve_default=False,
        ),
    ]

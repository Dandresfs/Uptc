# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('preventivo', '0005_eventcalendar_color'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventcalendar',
            name='icono',
            field=models.CharField(verbose_name='Icono', max_length=100, blank=True, null=True),
        ),
    ]

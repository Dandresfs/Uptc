# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('preventivo', '0002_eventcalendar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventcalendar',
            name='end',
            field=models.CharField(blank=True, null=True, max_length=100, verbose_name='Fin'),
        ),
    ]

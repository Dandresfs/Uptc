# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('preventivo', '0004_auto_20150725_2322'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventcalendar',
            name='color',
            field=models.CharField(max_length=100, blank=True, verbose_name='Color', null=True),
        ),
    ]

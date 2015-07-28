# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('preventivo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tipomantenimiento',
            name='plan',
            field=models.FileField(upload_to='Plan/', verbose_name='Plan', blank=True),
        ),
    ]

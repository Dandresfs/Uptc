# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('preventivo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventCalendar',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('title', models.CharField(verbose_name='Titulo', max_length=100)),
                ('start', models.CharField(verbose_name='Inicio', max_length=100)),
                ('end', models.CharField(verbose_name='Fin', max_length=100)),
            ],
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movBrasil_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='curso_model',
            options={'ordering': ('titulo',), 'verbose_name_plural': 'Cursos'},
        ),
        migrations.AddField(
            model_name='palestrantes_model',
            name='data',
            field=models.DateField(default='2014-12-12'),
            preserve_default=False,
        ),
    ]

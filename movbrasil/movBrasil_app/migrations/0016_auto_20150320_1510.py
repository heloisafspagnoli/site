# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movBrasil_app', '0015_auto_20150112_2308'),
    ]

    operations = [
        migrations.RenameField(
            model_name='curso_model',
            old_name='data',
            new_name='data_inicio',
        ),
        migrations.AddField(
            model_name='curso_model',
            name='data_final',
            field=models.DateField(default='2015-12-12'),
            preserve_default=False,
        ),
    ]

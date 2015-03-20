# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movBrasil_app', '0017_auto_20150320_1525'),
    ]

    operations = [
        migrations.RenameField(
            model_name='curso_model',
            old_name='data',
            new_name='data_inicial',
        ),
        migrations.AddField(
            model_name='curso_model',
            name='data_final',
            field=models.DateField(default='2015-12-12'),
            preserve_default=False,
        ),
    ]

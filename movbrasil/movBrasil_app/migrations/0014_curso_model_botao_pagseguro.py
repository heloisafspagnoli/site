# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movBrasil_app', '0013_auto_20150112_0036'),
    ]

    operations = [
        migrations.AddField(
            model_name='curso_model',
            name='botao_pagSeguro',
            field=models.CharField(default='teste', max_length=1000),
            preserve_default=False,
        ),
    ]

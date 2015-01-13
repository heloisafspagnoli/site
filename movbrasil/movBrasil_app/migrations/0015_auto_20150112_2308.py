# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movBrasil_app', '0014_curso_model_botao_pagseguro'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curso_model',
            name='botao_pagSeguro',
            field=models.TextField(),
            preserve_default=True,
        ),
    ]

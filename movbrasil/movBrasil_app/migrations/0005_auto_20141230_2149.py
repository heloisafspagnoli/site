# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movBrasil_app', '0004_endereco_contato_model_assuntos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='endereco_contato_model',
            name='telefone',
            field=models.CharField(max_length=30),
            preserve_default=True,
        ),
    ]

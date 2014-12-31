# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movBrasil_app', '0003_auto_20141230_2007'),
    ]

    operations = [
        migrations.AddField(
            model_name='endereco_contato_model',
            name='assuntos',
            field=models.TextField(default='nada'),
            preserve_default=False,
        ),
    ]

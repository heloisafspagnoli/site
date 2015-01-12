# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movBrasil_app', '0011_auto_20150111_2039'),
    ]

    operations = [
        migrations.AddField(
            model_name='endereco_contato_model',
            name='texto_inicial',
            field=models.TextField(default='r'),
            preserve_default=False,
        ),
    ]

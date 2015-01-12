# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movBrasil_app', '0012_endereco_contato_model_texto_inicial'),
    ]

    operations = [
        migrations.AddField(
            model_name='local_model',
            name='latitude',
            field=models.CharField(default='1', max_length=100, blank=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='local_model',
            name='longitude',
            field=models.CharField(default=1, max_length=100, blank=True),
            preserve_default=False,
        ),
    ]

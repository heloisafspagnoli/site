# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movBrasil_app', '0021_auto_20150322_1912'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='endereco_contato_model',
            name='telefone',
        ),
        migrations.AlterField(
            model_name='chamada_model',
            name='txt_botao2',
            field=models.CharField(max_length=50, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='chamada_model',
            name='url_botao2',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
    ]

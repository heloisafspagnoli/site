# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movBrasil_app', '0019_auto_20150320_1649'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='chamada_model',
            options={'verbose_name_plural': 'Chamadas'},
        ),
        migrations.AddField(
            model_name='chamada_model',
            name='titulo',
            field=models.CharField(default='teste', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='chamada_model',
            name='txt_botao1',
            field=models.CharField(default='oi', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='chamada_model',
            name='txt_botao2',
            field=models.CharField(default='tchau', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='chamada_model',
            name='url_botao1',
            field=models.TextField(default='oi'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='chamada_model',
            name='url_botao2',
            field=models.TextField(default='tchau'),
            preserve_default=False,
        ),
    ]

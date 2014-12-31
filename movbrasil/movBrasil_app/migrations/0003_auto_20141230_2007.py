# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movBrasil_app', '0002_auto_20141230_1942'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='programacao_model',
            options={'ordering': ('data', 'atividade'), 'verbose_name_plural': 'Programa\xe7\xe3o'},
        ),
        migrations.RemoveField(
            model_name='programacao_model',
            name='models_atividade',
        ),
        migrations.DeleteModel(
            name='atividades_model',
        ),
        migrations.RemoveField(
            model_name='programacao_model',
            name='palestrantes',
        ),
        migrations.AddField(
            model_name='curso_model',
            name='palestrantes',
            field=models.ManyToManyField(to='movBrasil_app.palestrantes_model'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='programacao_model',
            name='atividade',
            field=models.TextField(default='try'),
            preserve_default=False,
        ),
    ]

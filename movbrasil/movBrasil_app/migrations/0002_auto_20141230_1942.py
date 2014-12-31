# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movBrasil_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='atividades_model',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('hora', models.TimeField()),
                ('atividade', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name_plural': 'Atividades',
            },
            bases=(models.Model,),
        ),
        migrations.AlterModelOptions(
            name='programacao_model',
            options={'ordering': ('data',), 'verbose_name_plural': 'Programa\xe7\xe3o'},
        ),
        migrations.RemoveField(
            model_name='programacao_model',
            name='atividade',
        ),
        migrations.RemoveField(
            model_name='programacao_model',
            name='hora',
        ),
        migrations.AddField(
            model_name='programacao_model',
            name='models_atividade',
            field=models.ManyToManyField(to='movBrasil_app.atividades_model'),
            preserve_default=True,
        ),
    ]

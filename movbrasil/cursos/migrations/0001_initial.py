# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='curso_model',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titulo', models.CharField(max_length=254)),
                ('img_curso', models.ImageField(null=True, upload_to=b'', blank=True)),
                ('resumo', models.TextField(null=True, blank=True)),
                ('objetivos', models.TextField(null=True, blank=True)),
                ('carga_horaria', models.CharField(max_length=100)),
                ('publico', models.CharField(max_length=100)),
                ('ativo', models.BooleanField(default=True)),
            ],
            options={
                'ordering': ('titulo',),
                'verbose_name_plural': 'Curso',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='local_model',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome_local', models.CharField(max_length=200)),
                ('complemento', models.CharField(max_length=20, blank=True)),
                ('numero', models.CharField(max_length=20)),
                ('endereco', models.CharField(max_length=200)),
                ('bairro', models.CharField(max_length=100)),
                ('cidade', models.CharField(max_length=100)),
                ('estado', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Local',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='palestrantes_model',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=200)),
                ('resumo', models.TextField()),
                ('foto', models.ImageField(null=True, upload_to=b'', blank=True)),
            ],
            options={
                'ordering': ('nome',),
                'verbose_name_plural': 'Palestrantes',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='programacao_model',
            fields=[
                ('data', models.DateField()),
                ('hora', models.TimeField()),
                ('atividade', models.CharField(max_length=200)),
                ('curso', models.OneToOneField(primary_key=True, serialize=False, to='cursos.curso_model')),
                ('palestrante', models.ManyToManyField(to='cursos.palestrantes_model')),
            ],
            options={
                'ordering': ('atividade',),
                'verbose_name_plural': 'Programa\xe7\xe3o',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='palestrantes_model',
            name='cursos',
            field=models.ManyToManyField(to='cursos.curso_model'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='curso_model',
            name='local',
            field=models.ForeignKey(to='cursos.local_model'),
            preserve_default=True,
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='chamada_model',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('chamada', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name_plural': 'Chamada',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='curso_model',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titulo', models.CharField(max_length=254)),
                ('img_curso', models.ImageField(null=True, upload_to=b'', blank=True)),
                ('resumo', models.CharField(max_length=400)),
                ('descricao', models.TextField(null=True, blank=True)),
                ('material_incluso', models.TextField(null=True, blank=True)),
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
            name='endereco_contato_model',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('endereco', models.CharField(max_length=200)),
                ('e_mail', models.EmailField(max_length=75)),
                ('telefone', models.CharField(max_length=15)),
            ],
            options={
                'verbose_name_plural': 'Endere\xe7o e contato da empresa',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='equipe_model',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=200)),
                ('tel', models.CharField(max_length=11)),
                ('e_mail', models.EmailField(max_length=75)),
                ('foto', models.ImageField(null=True, upload_to=b'', blank=True)),
            ],
            options={
                'verbose_name_plural': 'Equipe',
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
            name='parceiros_model',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=200)),
                ('foto', models.ImageField(upload_to=b'')),
            ],
            options={
                'verbose_name_plural': 'Parceiros',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='programacao_model',
            fields=[
                ('data', models.DateField()),
                ('hora', models.TimeField()),
                ('atividade', models.CharField(max_length=200)),
                ('curso', models.OneToOneField(primary_key=True, serialize=False, to='movBrasil_app.curso_model')),
                ('palestrante', models.ManyToManyField(to='movBrasil_app.palestrantes_model')),
            ],
            options={
                'ordering': ('atividade',),
                'verbose_name_plural': 'Programa\xe7\xe3o',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='quem_somos_model',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descricao', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'Quem somos',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='palestrantes_model',
            name='cursos',
            field=models.ManyToManyField(to='movBrasil_app.curso_model'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='curso_model',
            name='local',
            field=models.ForeignKey(to='movBrasil_app.local_model'),
            preserve_default=True,
        ),
    ]

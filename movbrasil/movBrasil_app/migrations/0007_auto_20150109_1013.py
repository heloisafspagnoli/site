# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movBrasil_app', '0006_curso_model_preco'),
    ]

    operations = [
        migrations.CreateModel(
            name='img_qms_model',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=200)),
                ('img', models.ImageField(upload_to=b'')),
            ],
            options={
                'verbose_name_plural': 'Imagens Quem somos',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='chamada_model',
            name='img_chamada',
            field=models.ImageField(default='./2_2DGxJPg.jpg', upload_to=b''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='quem_somos_model',
            name='img',
            field=models.ManyToManyField(to='movBrasil_app.img_qms_model'),
            preserve_default=True,
        ),
    ]

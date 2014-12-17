# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dados_basicos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='time',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=200)),
                ('tel', models.CharField(max_length=11)),
                ('e_mail', models.EmailField(max_length=75)),
                ('foto', models.ImageField(height_field=200, width_field=200, upload_to=b'')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]

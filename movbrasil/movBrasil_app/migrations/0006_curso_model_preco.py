# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movBrasil_app', '0005_auto_20141230_2149'),
    ]

    operations = [
        migrations.AddField(
            model_name='curso_model',
            name='preco',
            field=models.CharField(default='1.000', max_length=300),
            preserve_default=False,
        ),
    ]

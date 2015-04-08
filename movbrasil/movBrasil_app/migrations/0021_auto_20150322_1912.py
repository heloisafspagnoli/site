# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movBrasil_app', '0020_auto_20150322_1300'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chamada_model',
            name='txt_botao2',
            field=models.CharField(max_length=50, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='chamada_model',
            name='url_botao2',
            field=models.TextField(blank=True),
            preserve_default=True,
        ),
    ]

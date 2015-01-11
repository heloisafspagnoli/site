# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movBrasil_app', '0010_auto_20150111_1314'),
    ]

    operations = [
        migrations.AddField(
            model_name='equipe_model',
            name='cargo',
            field=models.CharField(default='teste', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='quem_somos_model',
            name='nossa_missao',
            field=models.TextField(default='teste'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='quem_somos_model',
            name='nossa_visao',
            field=models.TextField(default='treste'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='quem_somos_model',
            name='somos_bons',
            field=models.TextField(default='xb'),
            preserve_default=False,
        ),
    ]

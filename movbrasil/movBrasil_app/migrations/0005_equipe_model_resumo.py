# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movBrasil_app', '0004_auto_20141226_0117'),
    ]

    operations = [
        migrations.AddField(
            model_name='equipe_model',
            name='resumo',
            field=models.TextField(default='teste', max_length=300),
            preserve_default=False,
        ),
    ]

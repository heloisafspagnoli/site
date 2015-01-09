# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movBrasil_app', '0007_auto_20150109_1013'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='curso_model',
            name='resumo',
        ),
        migrations.AddField(
            model_name='curso_model',
            name='tema',
            field=models.CharField(default='fisio', max_length=254),
            preserve_default=False,
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movBrasil_app', '0002_auto_20141226_0029'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='palestrantes_model',
            name='data',
        ),
        migrations.AddField(
            model_name='curso_model',
            name='data',
            field=models.DateField(default='2014-12-12'),
            preserve_default=False,
        ),
    ]

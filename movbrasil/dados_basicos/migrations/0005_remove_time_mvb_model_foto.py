# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dados_basicos', '0004_auto_20141216_2032'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='time_mvb_model',
            name='foto',
        ),
    ]

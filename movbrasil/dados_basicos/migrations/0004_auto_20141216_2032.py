# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dados_basicos', '0003_auto_20141216_1801'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='quem_somos',
            new_name='quem_somos_model',
        ),
        migrations.RenameModel(
            old_name='time_mvb',
            new_name='time_mvb_model',
        ),
    ]

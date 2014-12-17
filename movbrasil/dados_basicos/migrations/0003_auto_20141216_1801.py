# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dados_basicos', '0002_time'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='time',
            new_name='time_mvb',
        ),
    ]

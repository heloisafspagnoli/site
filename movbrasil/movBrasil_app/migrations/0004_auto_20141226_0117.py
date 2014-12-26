# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movBrasil_app', '0003_auto_20141226_0030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chamada_model',
            name='chamada',
            field=models.TextField(max_length=200),
            preserve_default=True,
        ),
    ]

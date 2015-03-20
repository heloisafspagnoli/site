# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movBrasil_app', '0018_auto_20150320_1533'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='endereco_contato_model',
            name='e_mail',
        ),
        migrations.AddField(
            model_name='equipe_model',
            name='contato',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]

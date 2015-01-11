# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movBrasil_app', '0009_auto_20150111_1307'),
    ]

    operations = [
        migrations.RenameField(
            model_name='quem_somos_model',
            old_name='img_qms',
            new_name='img',
        ),
    ]

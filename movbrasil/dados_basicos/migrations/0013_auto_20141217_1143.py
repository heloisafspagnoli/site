# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dados_basicos', '0012_auto_20141217_1112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='time_mvb_model',
            name='foto',
            field=models.ImageField(null=True, upload_to=b'/home/heloisa/Source/try/movbrasil/movbrasil/media/time_mvb/', blank=True),
            preserve_default=True,
        ),
    ]

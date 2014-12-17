# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dados_basicos', '0006_time_mvb_model_foto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='time_mvb_model',
            name='foto',
            field=models.ImageField(default=b'../../pic_folder/None/no-img.jpg', upload_to=b'../../pic_folder/'),
            preserve_default=True,
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dados_basicos', '0007_auto_20141217_0046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='time_mvb_model',
            name='foto',
            field=models.ImageField(default=b'../../pic_folder/no-img.jpg', upload_to=b'../../pic_folder/'),
            preserve_default=True,
        ),
    ]

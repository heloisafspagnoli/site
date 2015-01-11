# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movBrasil_app', '0008_auto_20150109_1535'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quem_somos_model',
            name='img',
        ),
        migrations.DeleteModel(
            name='img_qms_model',
        ),
        migrations.AddField(
            model_name='quem_somos_model',
            name='img_qms',
            field=models.ImageField(default='media/06.jpg', upload_to=b''),
            preserve_default=False,
        ),
    ]

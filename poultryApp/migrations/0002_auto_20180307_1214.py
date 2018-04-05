# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('poultryApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='data',
            name='Restart_no',
            field=models.IntegerField(max_length=11, default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='data',
            name='Restart_time',
            field=models.TimeField(default=0),
            preserve_default=False,
        ),
    ]

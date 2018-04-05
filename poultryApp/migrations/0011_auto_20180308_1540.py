# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('poultryApp', '0010_auto_20180308_1216'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='Cur_time',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='Restart_time',
            field=models.TimeField(blank=True, null=True),
        ),
    ]

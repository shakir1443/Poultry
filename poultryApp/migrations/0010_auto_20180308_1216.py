# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('poultryApp', '0009_auto_20180308_1214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='Cur_time',
            field=models.CharField(max_length=100, default=''),
        ),
    ]

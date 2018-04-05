# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('poultryApp', '0007_auto_20180307_1220'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='Cur_time',
            field=models.TimeField(default=datetime.time(0, 0)),
        ),
    ]

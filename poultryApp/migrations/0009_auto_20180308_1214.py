# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('poultryApp', '0008_auto_20180308_1156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='Cur_time',
            field=models.TimeField(default=''),
        ),
    ]

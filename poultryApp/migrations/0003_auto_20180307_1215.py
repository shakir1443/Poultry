# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('poultryApp', '0002_auto_20180307_1214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='Restart_no',
            field=models.IntegerField(max_length=111),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('poultryApp', '0006_auto_20180307_1216'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='Day',
            field=models.IntegerField(max_length=11),
        ),
        migrations.AlterField(
            model_name='data',
            name='Restart_no',
            field=models.IntegerField(max_length=11),
        ),
    ]

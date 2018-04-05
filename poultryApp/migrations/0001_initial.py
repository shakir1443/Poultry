# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='data',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('Day', models.IntegerField(max_length=11)),
                ('Temperature', models.FloatField(max_length=50)),
                ('Humidity', models.FloatField(max_length=50)),
                ('Carbon_dy_oxide', models.FloatField(max_length=50)),
                ('Amonia', models.FloatField(max_length=50)),
                ('ADC', models.CharField(max_length=100)),
                ('Light_status', models.CharField(max_length=100)),
                ('Fan_status', models.CharField(max_length=100)),
                ('Start_date', models.DateField()),
                ('Cur_Date', models.DateField()),
                ('Cur_time', models.TimeField()),
            ],
            options={
                'db_table': 'data',
            },
        ),
    ]

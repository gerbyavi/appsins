# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('datt', models.DateField()),
                ('asin', models.CharField(default='', max_length=10)),
                ('rank', models.IntegerField(default=0)),
                ('name', models.TextField(default='')),
                ('cmpt', models.IntegerField(default=0)),
                ('nfl', models.IntegerField(default=0)),
                ('calc', models.DecimalField(default=0.0, max_digits=5, decimal_places=2)),
                ('minprice', models.DecimalField(default=0.0, max_digits=5, decimal_places=2)),
                ('minpriceful', models.DecimalField(default=0.0, max_digits=5, decimal_places=2)),
                ('cost', models.DecimalField(default=0.0, max_digits=5, decimal_places=2)),
                ('clcminuscost', models.DecimalField(default=0.0, max_digits=5, decimal_places=2)),
                ('precentprof', models.DecimalField(default=0.0, max_digits=5, decimal_places=2)),
            ],
        ),
    ]

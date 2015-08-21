# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Estadiamento',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cid', models.CharField(max_length=50)),
                ('t', models.CharField(max_length=5)),
                ('n', models.CharField(max_length=5)),
                ('m', models.CharField(max_length=5)),
            ],
        ),
    ]

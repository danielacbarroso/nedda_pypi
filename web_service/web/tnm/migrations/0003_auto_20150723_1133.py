# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tnm', '0002_resultado'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cid',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cid', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Tnm',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('m', models.ManyToManyField(related_name='Tnm.m+', to='tnm.Cid')),
                ('n', models.ManyToManyField(related_name='Tnm.n+', to='tnm.Cid')),
                ('t', models.ManyToManyField(related_name='Tnm.t+', to='tnm.Cid')),
            ],
        ),
        migrations.DeleteModel(
            name='Estadiamento',
        ),
    ]

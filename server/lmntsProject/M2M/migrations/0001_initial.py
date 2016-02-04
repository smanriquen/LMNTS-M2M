# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='characteristics',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('characteristicType', models.CharField(max_length=140, blank=True)),
                ('value', models.CharField(max_length=140, blank=True)),
                ('timer', models.CharField(max_length=140, blank=True)),
                ('lastRead', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='machine',
            fields=[
                ('machineType', models.CharField(max_length=140, blank=True)),
                ('family', models.CharField(max_length=140, blank=True)),
                ('serial', models.CharField(max_length=100, serialize=False, primary_key=True)),
                ('MAC', models.CharField(max_length=20, blank=True)),
                ('services', models.TextField(null=True, blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='characteristics',
            name='parent',
            field=models.ForeignKey(related_name='characteristics', blank=True, to='M2M.machine'),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-26 16:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proyecto', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proyectogrado',
            name='comentario',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]

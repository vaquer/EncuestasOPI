# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-10-06 18:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('encuestas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='encuesta',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]

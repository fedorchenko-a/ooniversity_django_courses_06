# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-25 19:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='order',
            field=models.PositiveIntegerField(default='0'),
            preserve_default=False,
        ),
    ]

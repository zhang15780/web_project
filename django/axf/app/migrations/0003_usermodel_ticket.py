# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-07 10:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_mainshop'),
    ]

    operations = [
        migrations.AddField(
            model_name='usermodel',
            name='ticket',
            field=models.CharField(max_length=255, null=True),
        ),
    ]

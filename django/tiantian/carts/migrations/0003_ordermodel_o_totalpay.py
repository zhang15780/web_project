# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-18 11:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0002_ordermodel_o_addr'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordermodel',
            name='o_totalpay',
            field=models.CharField(max_length=255, null=True),
        ),
    ]

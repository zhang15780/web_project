# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-17 12:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20180517_1947'),
    ]

    operations = [
        migrations.AddField(
            model_name='usersession',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.Users'),
        ),
    ]

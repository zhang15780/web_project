# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-17 11:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20180516_2051'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='addr',
        ),
        migrations.AddField(
            model_name='useraddr',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.Users'),
        ),
    ]

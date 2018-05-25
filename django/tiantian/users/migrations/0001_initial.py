# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-16 12:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserAddr',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rec_peo', models.CharField(max_length=50)),
                ('rec_addr', models.CharField(max_length=255)),
                ('rec_tel', models.CharField(max_length=11)),
                ('rec_code', models.IntegerField(max_length=10)),
            ],
            options={
                'db_table': 'day_addr',
            },
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('u_name', models.CharField(max_length=50, unique=True)),
                ('u_email', models.CharField(max_length=20)),
                ('u_pass', models.CharField(max_length=255)),
                ('u_create', models.DateTimeField(auto_now=True)),
                ('addr', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.UserAddr')),
            ],
            options={
                'db_table': 'day_users',
            },
        ),
        migrations.CreateModel(
            name='UserSession',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('out_time', models.DateTimeField()),
                ('ticket', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'day_usersessions',
            },
        ),
    ]

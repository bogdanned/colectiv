# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-20 19:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_index', '0004_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='route',
            name='email',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app_index.Email'),
        ),
    ]

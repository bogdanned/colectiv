# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-11 18:43
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Route',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Creation Date')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Updated')),
                ('destiny', models.CharField(blank=True, max_length=3000, null=True)),
                ('origin', models.CharField(blank=True, max_length=3000, null=True)),
                ('duration', models.DurationField(blank=True, null=True)),
                ('distance', models.CharField(blank=True, max_length=3000, null=True)),
                ('user', models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Ruta Colectiv',
                'verbose_name_plural': 'Ruta Colectiv',
            },
        ),
    ]

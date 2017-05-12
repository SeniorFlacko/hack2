# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-12 01:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('cover', models.URLField(max_length=120)),
                ('isbn', models.CharField(max_length=120)),
                ('uri', models.CharField(max_length=120)),
                ('author', models.CharField(max_length=120)),
            ],
        ),
    ]

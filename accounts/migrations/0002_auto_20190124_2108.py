# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-01-24 21:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar_url',
            field=models.CharField(blank=True, default='images/user.jpg', max_length=200),
        ),
    ]
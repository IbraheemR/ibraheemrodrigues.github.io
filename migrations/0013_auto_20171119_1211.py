# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-19 12:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_auto_20171119_1207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='icon',
            field=models.ImageField(blank=True, upload_to='images'),
        ),
    ]
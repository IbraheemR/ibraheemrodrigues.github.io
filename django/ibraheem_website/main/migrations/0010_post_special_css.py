# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-19 11:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_post_extra_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='special_css',
            field=models.CharField(blank=True, max_length=10000),
        ),
    ]

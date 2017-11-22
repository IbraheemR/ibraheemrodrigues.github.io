# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-20 17:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_auto_20171119_1231'),
    ]

    operations = [
        migrations.AddField(
            model_name='galleryimage',
            name='hidden',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='post',
            name='hidden',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='galleryimage',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='post',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-28 05:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0002_artist_youtube'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='youtube',
            field=models.URLField(max_length=500, null=True),
        ),
    ]
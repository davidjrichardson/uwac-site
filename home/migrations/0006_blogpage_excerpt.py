# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-21 22:04
from __future__ import unicode_literals

from django.db import migrations
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_blogpage'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpage',
            name='excerpt',
            field=wagtail.fields.RichTextField(default='', help_text='This is displayed on the home and blog listing pages'),
        ),
    ]

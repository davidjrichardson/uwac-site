# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-12-21 18:47
from __future__ import unicode_literals

from django.db import migrations
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_homepage_cover_image_credit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='galleryindexpage',
            name='description',
            field=wagtail.fields.RichTextField(blank=True, default=''),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-12-23 15:26
from __future__ import unicode_literals

from django.db import migrations
import wagtail.contrib.table_block.blocks
import wagtail.blocks
import wagtail.fields
import wagtail.documents.blocks
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_auto_20171221_1847'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpage',
            name='body',
            field=wagtail.fields.StreamField((('h2', wagtail.blocks.CharBlock(classname='title', icon='title')), ('h3', wagtail.blocks.CharBlock(classname='title', icon='title')), ('h4', wagtail.blocks.CharBlock(classname='title', icon='title')), ('paragraph', wagtail.blocks.RichTextBlock(icon='pilcrow')), ('image', wagtail.blocks.StructBlock((('image', wagtail.images.blocks.ImageChooserBlock()), ('credit', wagtail.blocks.TextBlock(help_text='Image credit'))))), ('pullquote', wagtail.blocks.StructBlock((('quote', wagtail.blocks.TextBlock('quote title')), ('attribution', wagtail.blocks.CharBlock())))), ('gallery', wagtail.blocks.StructBlock((('gallery', wagtail.blocks.PageChooserBlock(target_model=['home.GalleryPage'])),))), ('document', wagtail.documents.blocks.DocumentChooserBlock(icon='doc-full-inverse')), ('table', wagtail.contrib.table_block.blocks.TableBlock(table_options={'startCols': 2, 'startRows': 1})))),
        ),
    ]

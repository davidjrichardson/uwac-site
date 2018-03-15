# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-01-14 21:42
from __future__ import unicode_literals

from django.db import migrations
import wagtail.contrib.table_block.blocks
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.documents.blocks
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0017_remove_contentpage_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpage',
            name='body',
            field=wagtail.core.fields.StreamField((('h2', wagtail.core.blocks.CharBlock(classname='title', icon='title')), ('h3', wagtail.core.blocks.CharBlock(classname='title', icon='title')), ('h4', wagtail.core.blocks.CharBlock(classname='title', icon='title')), ('paragraph', wagtail.core.blocks.RichTextBlock(icon='pilcrow')), ('credit_image', wagtail.core.blocks.StructBlock((('image', wagtail.images.blocks.ImageChooserBlock()), ('caption', wagtail.core.blocks.TextBlock(help_text='Photo caption', required=False)), ('credit', wagtail.core.blocks.TextBlock(help_text='Image credit'))))), ('image', wagtail.images.blocks.ImageChooserBlock()), ('pullquote', wagtail.core.blocks.StructBlock((('quote', wagtail.core.blocks.TextBlock('quote title')), ('attribution', wagtail.core.blocks.CharBlock())))), ('gallery', wagtail.core.blocks.StructBlock((('gallery', wagtail.core.blocks.PageChooserBlock(target_model=['home.GalleryPage'])),))), ('document', wagtail.documents.blocks.DocumentChooserBlock(icon='doc-full-inverse')), ('table', wagtail.contrib.table_block.blocks.TableBlock(table_options={'startCols': 2, 'startRows': 1})))),
        ),
        migrations.AlterField(
            model_name='contentpage',
            name='body',
            field=wagtail.core.fields.StreamField((('h2', wagtail.core.blocks.CharBlock(classname='title', icon='title')), ('h3', wagtail.core.blocks.CharBlock(classname='title', icon='title')), ('h4', wagtail.core.blocks.CharBlock(classname='title', icon='title')), ('paragraph', wagtail.core.blocks.RichTextBlock(icon='pilcrow')), ('credit_image', wagtail.core.blocks.StructBlock((('image', wagtail.images.blocks.ImageChooserBlock()), ('caption', wagtail.core.blocks.TextBlock(help_text='Photo caption', required=False)), ('credit', wagtail.core.blocks.TextBlock(help_text='Image credit'))))), ('image', wagtail.images.blocks.ImageChooserBlock()), ('pullquote', wagtail.core.blocks.StructBlock((('quote', wagtail.core.blocks.TextBlock('quote title')), ('attribution', wagtail.core.blocks.CharBlock())))), ('gallery', wagtail.core.blocks.StructBlock((('gallery', wagtail.core.blocks.PageChooserBlock(target_model=['home.GalleryPage'])),))), ('document', wagtail.documents.blocks.DocumentChooserBlock(icon='doc-full-inverse')), ('table', wagtail.contrib.table_block.blocks.TableBlock(table_options={'startCols': 2, 'startRows': 1})))),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-19 16:53
from __future__ import unicode_literals

import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields
from django.db import migrations

import images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0010_auto_20161221_1701'),
    ]

    operations = [
        migrations.AlterField(
            model_name='editorialpage',
            name='main',
            field=wagtail.wagtailcore.fields.StreamField((('markdown', wagtail.wagtailcore.blocks.RichTextBlock(icon='radio-full', label='markdown')), ('figureList', wagtail.wagtailcore.blocks.ListBlock(images.blocks.ImageChooserBlock(), icon='radio-full', label='figure list')), ('panel', wagtail.wagtailcore.blocks.StructBlock((('main', wagtail.wagtailcore.blocks.RichTextBlock(label='Panel content')), ('footer', wagtail.wagtailcore.blocks.RichTextBlock(label='Footer content', required=False))), icon='radio-full', label='panel')), ('splitPanel', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.RichTextBlock(), icon='radio-full', label='split panel'))), blank=True, null=True, verbose_name='Main Content'),
        ),
    ]

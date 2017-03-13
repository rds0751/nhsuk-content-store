# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-09 14:35
from __future__ import unicode_literals

import json

from django.core.serializers.json import DjangoJSONEncoder
from django.db import migrations
from django.utils.timezone import now
from modelcluster.models import (
    get_all_child_m2m_relations, get_all_child_relations,
    get_serializable_data_for_fields
)


def serializable_data(page):
    obj = get_serializable_data_for_fields(page)

    for rel in get_all_child_relations(page):
        rel_name = rel.get_accessor_name()
        children = getattr(page, rel_name).all()

        if hasattr(rel.related_model, 'serializable_data'):
            obj[rel_name] = [child.serializable_data() for child in children]
        else:
            obj[rel_name] = [get_serializable_data_for_fields(child) for child in children]

    for field in get_all_child_m2m_relations(page):
        children = getattr(page, field.name).all()
        obj[field.name] = [child.pk for child in children]

    return obj


def to_json(page):
    return json.dumps(serializable_data(page), cls=DjangoJSONEncoder)


def forwards_func(apps, schema_editor):
    # Get models
    Page = apps.get_model('wagtailcore.Page')

    # create a revision for the conditions page
    conditions_page = Page.objects.get(slug='conditions')
    dt_now = now()
    if not conditions_page.revisions.count():
        conditions_page.revisions.create(
            content_json=to_json(conditions_page),
            created_at=dt_now
        )
        conditions_page.latest_revision_created_at = dt_now
        conditions_page.save(update_fields=['latest_revision_created_at'])

    # create a revision for the symptoms page
    symptoms_page = Page.objects.get(slug='symptoms')
    if not symptoms_page.revisions.count():
        symptoms_page.revisions.create(
            content_json=to_json(symptoms_page),
            created_at=dt_now
        )
        symptoms_page.latest_revision_created_at = dt_now
        symptoms_page.save(update_fields=['latest_revision_created_at'])


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0015_auto_20170227_1718'),
    ]

    operations = [
        migrations.RunPython(forwards_func),
    ]
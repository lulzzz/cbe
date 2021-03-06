# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-05 11:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import gm2m.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Buyer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valid_from', models.DateTimeField(auto_now_add=True)),
                ('valid_to', models.DateTimeField(blank=True, null=True)),
                ('name', models.CharField(max_length=200)),
                ('party_object_id', models.PositiveIntegerField()),
                ('contact_mediums', gm2m.fields.GM2MField(through_fields=('gm2m_src', 'gm2m_tgt', 'gm2m_ct', 'gm2m_pk'))),
                ('party_content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='supplier_partner_buyer_ownership', to='contenttypes.ContentType')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Partner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valid_from', models.DateTimeField(auto_now_add=True)),
                ('valid_to', models.DateTimeField(blank=True, null=True)),
                ('name', models.CharField(max_length=200)),
                ('party_object_id', models.PositiveIntegerField()),
                ('contact_mediums', gm2m.fields.GM2MField(through_fields=('gm2m_src', 'gm2m_tgt', 'gm2m_ct', 'gm2m_pk'))),
                ('party_content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='supplier_partner_partner_ownership', to='contenttypes.ContentType')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valid_from', models.DateTimeField(auto_now_add=True)),
                ('valid_to', models.DateTimeField(blank=True, null=True)),
                ('name', models.CharField(max_length=200)),
                ('party_object_id', models.PositiveIntegerField()),
                ('contact_mediums', gm2m.fields.GM2MField(through_fields=('gm2m_src', 'gm2m_tgt', 'gm2m_ct', 'gm2m_pk'))),
                ('party_content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='supplier_partner_supplier_ownership', to='contenttypes.ContentType')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]

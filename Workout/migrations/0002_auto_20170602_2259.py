# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-03 03:59
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Workout', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='patient',
            old_name='patient_id',
            new_name='patient_loginName',
        ),
    ]
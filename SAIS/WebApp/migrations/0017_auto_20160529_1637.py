# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-29 08:37
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('WebApp', '0016_student_user_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='schedule',
            old_name='schedule_id',
            new_name='subject_id',
        ),
        migrations.RemoveField(
            model_name='subjects',
            name='schedule_id',
        ),
    ]

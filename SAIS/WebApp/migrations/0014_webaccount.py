# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-28 05:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('WebApp', '0013_remove_student_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='WebAccount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(blank=True, max_length=30, null=True)),
                ('email', models.CharField(blank=True, max_length=30, null=True)),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='WebApp.Student')),
            ],
        ),
    ]
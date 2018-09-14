# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-07-29 13:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('issuetracker', '0004_data_migration_set_bugzilla_to_allow_add_case_to_issue'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='issuetracker',
            name='issue_report_fmt',
        ),
        migrations.AddField(
            model_name='issuetracker',
            name='issue_report_templ',
            field=models.CharField(blank=True, default='', help_text='The issue content template, which could be arbitrary text with format arguments. Nitrate provides these format arguments: <code>TestBuild.name</code>, <code>setup</code>, <code>action</code> and <code>effect</code>. The text is formatted with keyward arguments.', max_length=255),
        ),
        migrations.AlterField(
            model_name='issuetracker',
            name='issue_report_params',
            field=models.CharField(blank=True, default='', help_text='Parameters used to format URL for reporting issue. Each line is a <code>key:value</code> pair of parameters. Nitrate provides a few parameters to format URL and additional parameters could be provided by system administrator as well. ', max_length=255),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-05 01:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ToDoList', '0006_auto_20160625_0054'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='task',
        ),
        migrations.RemoveField(
            model_name='task',
            name='taskName',
        ),
        migrations.AddField(
            model_name='task',
            name='taskDescription',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Item',
        ),
    ]

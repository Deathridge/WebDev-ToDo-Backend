# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-24 16:19
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ToDoList', '0004_item_creator'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='creator',
        ),
    ]
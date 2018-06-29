# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-25 01:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aristotle_mdr_slots', '0006_auto_20180531_0337'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slot',
            name='permission',
            field=models.IntegerField(choices=[(0, 'Public'), (1, 'Authenticated'), (2, 'Workgroup')], default=0),
        ),
    ]

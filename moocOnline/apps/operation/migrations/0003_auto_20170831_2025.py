# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-08-31 20:25
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('operation', '0002_auto_20170831_2003'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='usercourse',
            options={'verbose_name': '\u7528\u6237\u8bfe\u7a0b', 'verbose_name_plural': '\u7528\u6237\u8bfe\u7a0b'},
        ),
        migrations.AlterModelOptions(
            name='userfavorite',
            options={'verbose_name': '\u7528\u6237\u6536\u85cf', 'verbose_name_plural': '\u7528\u6237\u6536\u85cf'},
        ),
        migrations.AlterModelOptions(
            name='usermessage',
            options={'verbose_name': '\u7528\u6237\u4fe1\u606f', 'verbose_name_plural': '\u7528\u6237\u4fe1\u606f'},
        ),
    ]

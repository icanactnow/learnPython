# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-08-28 16:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0004_remove_courseorg_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='courseorg',
            name='category',
            field=models.CharField(choices=[(b'pxjg', b'\xe5\x9f\xb9\xe8\xae\xad\xe6\x9c\xba\xe6\x9e\x84'), (b'gx', b'\xe9\xab\x98\xe6\xa0\xa1'), (b'gr', b'\xe4\xb8\xaa\xe4\xba\xba')], default=b'pxjg', max_length=20, verbose_name=b'\xe6\x9c\xba\xe6\x9e\x84\xe7\xb1\xbb\xe5\x88\xab'),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-08-31 20:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_course_course_org'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.Course', verbose_name='\u7ae0\u8282\u6240\u5c5e\u8bfe\u7a0b'),
        ),
    ]

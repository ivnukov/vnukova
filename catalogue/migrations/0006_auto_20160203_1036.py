# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-03 10:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0005_auto_20160202_1546'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='imagename',
            field=models.FileField(blank=True, default='default.jpg', null=True, upload_to='static/images/catalogue/'),
        ),
    ]
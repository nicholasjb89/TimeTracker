# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-02 22:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('DevLog', '0003_auto_20160402_1826'),
    ]

    operations = [
        migrations.AddField(
            model_name='log',
            name='subject',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='DevLog.Subject'),
        ),
    ]
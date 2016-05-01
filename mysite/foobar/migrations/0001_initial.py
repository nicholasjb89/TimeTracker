# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-30 23:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Day',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('startTime', models.DateTimeField()),
                ('endTime', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='ScheduledEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eventStartTime', models.DateTimeField()),
                ('dayID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='foobar.Day')),
                ('eventID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='foobar.Event')),
                ('roomID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='foobar.Room')),
            ],
        ),
    ]
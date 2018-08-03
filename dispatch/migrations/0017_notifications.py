# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-11 20:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('dispatch', '0016_breaking_news'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('scheduled_push_time', models.DateTimeField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('endpoint', models.CharField(max_length=255, unique=True)),
                ('auth', models.CharField(max_length=255, unique=True)),
                ('p256dh', models.CharField(max_length=255, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ('created_at',),
            },
        ),
        migrations.AddField(
            model_name='article',
            name='scheduled_notification',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='notification',
            name='article',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notification_artilce', to='dispatch.Article'),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import ThriftServer.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hashtag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('hashtag', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='HashtagItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('hashtag_id', models.ForeignKey(to='ThriftServer.Hashtag')),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('status', models.CharField(max_length=255)),
                ('image1', models.ImageField(null=True, upload_to=ThriftServer.models.get_image_path, blank=True)),
                ('image2', models.ImageField(null=True, upload_to=ThriftServer.models.get_image_path, blank=True)),
                ('image3', models.ImageField(null=True, upload_to=ThriftServer.models.get_image_path, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
                ('image', models.ImageField(null=True, upload_to=ThriftServer.models.get_image_path, blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='item',
            name='req_id',
            field=models.ForeignKey(related_name='request', to='ThriftServer.User'),
        ),
        migrations.AddField(
            model_name='item',
            name='user_id',
            field=models.ForeignKey(related_name='user', to='ThriftServer.User'),
        ),
        migrations.AddField(
            model_name='hashtagitem',
            name='item_id',
            field=models.ForeignKey(to='ThriftServer.Item'),
        ),
    ]

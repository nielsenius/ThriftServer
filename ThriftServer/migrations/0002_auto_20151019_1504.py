# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ThriftServer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='req_id',
            field=models.ForeignKey(related_name='request', to='ThriftServer.User', null=True),
        ),
    ]

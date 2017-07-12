# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='caption',
            field=models.CharField(default=datetime.datetime(2017, 7, 12, 11, 0, 48, 711533, tzinfo=utc), max_length=200),
            preserve_default=False,
        ),
    ]

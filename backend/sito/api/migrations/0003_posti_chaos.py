# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20141108_1618'),
    ]

    operations = [
        migrations.AddField(
            model_name='posti',
            name='chaos',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]

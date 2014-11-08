# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='utenti',
            name='id',
        ),
        migrations.RemoveField(
            model_name='utenti',
            name='ip_address',
        ),
        migrations.AddField(
            model_name='utenti',
            name='code',
            field=models.CharField(default=b'aaa', max_length=20, serialize=False, primary_key=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='aule',
            name='nome',
            field=models.CharField(max_length=20),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='posti',
            name='timestamp',
            field=models.DateTimeField(auto_now=True),
            preserve_default=True,
        ),
    ]

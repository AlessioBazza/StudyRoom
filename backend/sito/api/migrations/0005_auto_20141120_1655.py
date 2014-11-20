# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_posti_lesson'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='posti',
            options={'ordering': ['-timestamp']},
        ),
        migrations.AlterField(
            model_name='posti',
            name='user',
            field=models.CharField(max_length=50),
            preserve_default=True,
        ),
        migrations.DeleteModel(
            name='Utenti',
        ),
    ]

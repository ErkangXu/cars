# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rental', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='violation',
            name='fine',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='violation',
            name='points',
            field=models.IntegerField(),
        ),
    ]

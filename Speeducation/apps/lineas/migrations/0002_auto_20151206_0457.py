# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lineas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='actividad',
            name='updated',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='conducta',
            name='updated',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='linea',
            name='updated',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]

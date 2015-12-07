# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('alumnos', '0013_auto_20151207_0411'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='alumno',
            name='sexo',
        ),
        migrations.AlterField(
            model_name='periodo',
            name='fechaFinal',
            field=models.DateField(default=datetime.datetime(2015, 12, 7, 4, 14, 50, 964110, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='periodo',
            name='fechaInicio',
            field=models.DateField(default=datetime.datetime(2015, 12, 7, 4, 14, 50, 964045, tzinfo=utc)),
        ),
    ]

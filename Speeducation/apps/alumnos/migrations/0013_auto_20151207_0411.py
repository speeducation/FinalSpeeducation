# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('alumnos', '0012_auto_20151207_0356'),
    ]

    operations = [
        migrations.AddField(
            model_name='alumno',
            name='sexo',
            field=models.CharField(default=((b'H', b'Hombre'), (b'M', b'Mujer')), max_length=50, null=True, choices=[(b'H', b'Hombre'), (b'M', b'Mujer')]),
        ),
        migrations.AlterField(
            model_name='periodo',
            name='fechaFinal',
            field=models.DateField(default=datetime.datetime(2015, 12, 7, 4, 11, 59, 121034, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='periodo',
            name='fechaInicio',
            field=models.DateField(default=datetime.datetime(2015, 12, 7, 4, 11, 59, 120989, tzinfo=utc)),
        ),
    ]

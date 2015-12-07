# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('lineas', '0002_auto_20151206_0457'),
        ('alumnos', '0011_auto_20151120_2144'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comportamiento',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('alumno', models.ForeignKey(to='alumnos.Alumno')),
                ('conducta', models.ForeignKey(to='lineas.Conducta')),
            ],
        ),
        migrations.CreateModel(
            name='Evaluacion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('finalizado', models.BooleanField(default=False)),
                ('evaluacionInicial', models.CharField(default=0, max_length=20, choices=[(b'Ineficiente', 1), (b'Bueno', 2), (b'Excelente', 3)])),
                ('evaluacionMedia', models.CharField(default=0, max_length=20, choices=[(b'Ineficiente', 1), (b'Bueno', 2), (b'Excelente', 3)])),
                ('evaluacionFinal', models.CharField(default=0, max_length=20, choices=[(b'Ineficiente', 1), (b'Bueno', 2), (b'Excelente', 3)])),
                ('actividad', models.ForeignKey(to='lineas.Actividad')),
            ],
        ),
        migrations.CreateModel(
            name='Periodo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fechaInicio', models.DateField(default=datetime.datetime(2015, 12, 7, 3, 56, 6, 781433, tzinfo=utc))),
                ('fechaFinal', models.DateField(default=datetime.datetime(2015, 12, 7, 3, 56, 6, 781482, tzinfo=utc))),
            ],
        ),
        migrations.CreateModel(
            name='PlanEstudio',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('alumno', models.ForeignKey(to='alumnos.Alumno')),
                ('linea', models.ForeignKey(to='lineas.Linea')),
                ('periodo', models.ForeignKey(default=b'', to='alumnos.Periodo')),
            ],
        ),
        migrations.AddField(
            model_name='evaluacion',
            name='plan',
            field=models.ForeignKey(default=b'', to='alumnos.PlanEstudio'),
        ),
    ]

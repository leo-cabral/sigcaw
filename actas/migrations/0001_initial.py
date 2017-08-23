# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-08-23 02:53
from __future__ import unicode_literals

import actas.models
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('personas', '0001_initial'),
        ('grados', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Acta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_libro', models.SmallIntegerField(default=actas.models.get_last_libro, verbose_name='Número de Libro')),
                ('numero_folio', models.SmallIntegerField(default=actas.models.get_last_folio, verbose_name='Número de Folio')),
                ('numero_acta', models.SmallIntegerField(default=actas.models.get_next_acta, verbose_name='Número de Acta')),
                ('fecha_acta', models.DateField(default=django.utils.timezone.now, verbose_name='Fecha de Acta')),
                ('descripcion_acta', models.CharField(max_length=1000, verbose_name='Descripción del Acta')),
            ],
            options={
                'ordering': ['numero_libro', 'numero_folio', 'numero_acta'],
            },
        ),
        migrations.CreateModel(
            name='Ascenso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bombero', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='personas.Bombero', verbose_name='Bombero Ascendido')),
                ('grado_ascenso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='grados.Grado', verbose_name='Grado Ascendido')),
            ],
            options={
                'ordering': ['acta_ascenso'],
            },
        ),
        migrations.CreateModel(
            name='Sancion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rol_incidente', models.CharField(max_length=1000, verbose_name='Rol que cumplió en el incidente')),
                ('descargo', models.TextField(blank=True, max_length=2000, null=True, verbose_name='Descargo presentado por el Bombero')),
                ('tipo_sancion', models.CharField(choices=[('advertencia', 'Advertencia'), ('suspencion', 'Suspención'), ('exoneracion', 'Exoneración')], default='advertencia', max_length=20, verbose_name='Tipo de Sanción disciplinaria')),
                ('dias_suspencion', models.SmallIntegerField(default=0, verbose_name='Días de Suspención')),
                ('fecha_efectiva', models.DateField(blank=True, null=True, verbose_name='Fecha en que se efectiviza la sanción')),
                ('bombero', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='personas.Bombero', verbose_name='Bombero interviniente')),
            ],
            options={
                'ordering': ['acta_sancion'],
            },
        ),
        migrations.CreateModel(
            name='ActaAscenso',
            fields=[
                ('acta_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='actas.Acta')),
                ('fecha_efectiva', models.DateField(verbose_name='Fecha efectiva de Ascenso')),
            ],
            options={
                'verbose_name_plural': 'Actas de Ascensos',
                'verbose_name': 'Acta de Ascenso',
            },
            bases=('actas.acta',),
        ),
        migrations.CreateModel(
            name='ActaSancion',
            fields=[
                ('acta_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='actas.Acta')),
                ('fecha_incidente', models.DateField(verbose_name='Fecha del Incidente')),
                ('descripcion_incidente', models.CharField(max_length=500, verbose_name='Descripción del Incidente')),
            ],
            options={
                'verbose_name_plural': 'Actas de Sanciones',
                'verbose_name': 'Acta de Sanción',
            },
            bases=('actas.acta',),
        ),
        migrations.CreateModel(
            name='Licencia',
            fields=[
                ('acta_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='actas.Acta')),
                ('fecha_desde', models.DateField(verbose_name='Fecha desde')),
                ('fecha_hasta', models.DateField(verbose_name='Fecha hasta')),
                ('motivo', models.CharField(max_length=500, verbose_name='Motivo de la Licencia')),
                ('bombero', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='personas.Bombero', verbose_name='Bombero')),
            ],
            bases=('actas.acta',),
        ),
        migrations.CreateModel(
            name='Pase',
            fields=[
                ('acta_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='actas.Acta')),
                ('fecha_efectiva', models.DateField(default=django.utils.timezone.now, verbose_name='Fecha en que se efectiviza el pase')),
                ('bombero', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='personas.Bombero', verbose_name='Bombero solicitante')),
                ('institucion_destino', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Institucion_Destino', to='personas.Institucion', verbose_name='Institución Destino')),
                ('institucion_origen', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Institucion_Origen', to='personas.Institucion', verbose_name='Institución Origen')),
            ],
            bases=('actas.acta',),
        ),
        migrations.CreateModel(
            name='Premio',
            fields=[
                ('acta_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='actas.Acta')),
                ('fecha_premiacion', models.DateField(verbose_name='Fecha de la premiación')),
                ('premio_otorgado', models.CharField(max_length=500, verbose_name='Premio Otorgado')),
                ('bombero', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='personas.Bombero', verbose_name='Bombero premiado')),
            ],
            bases=('actas.acta',),
        ),
        migrations.AlterUniqueTogether(
            name='acta',
            unique_together=set([('numero_libro', 'numero_folio', 'numero_acta')]),
        ),
        migrations.AddField(
            model_name='sancion',
            name='acta_sancion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='actas.ActaSancion', verbose_name='Acta de Sanción'),
        ),
        migrations.AddField(
            model_name='ascenso',
            name='acta_ascenso',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='actas.ActaAscenso', verbose_name='Acta de Ascenso'),
        ),
    ]

# Generated by Django 5.0.3 on 2024-05-23 21:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('telefono', models.CharField(max_length=20)),
                ('direccion', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dni', models.CharField(max_length=20, unique=True)),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('telefono', models.CharField(max_length=20)),
                ('responsable', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Participacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_participacion', models.DateField(auto_now_add=True)),
                ('empleado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DjangoGePrApp.empleado')),
            ],
        ),
        migrations.CreateModel(
            name='Proyecto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
                ('fecha_inicio', models.DateField()),
                ('fecha_fin', models.DateField()),
                ('presupuesto', models.DecimalField(decimal_places=2, max_digits=10)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='proyectos', to='DjangoGePrApp.cliente')),
            ],
        ),
        migrations.CreateModel(
            name='Tarea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
                ('fecha_inicio', models.DateField()),
                ('fecha_fin', models.DateField()),
                ('nivel_prioridad', models.IntegerField()),
                ('estado', models.CharField(max_length=50)),
                ('empleados', models.ManyToManyField(related_name='tareas', through='DjangoGePrApp.Participacion', to='DjangoGePrApp.empleado')),
                ('proyecto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tareas', to='DjangoGePrApp.proyecto')),
                ('responsable', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='tareas_responsables', to='DjangoGePrApp.empleado')),
            ],
        ),
        migrations.AddField(
            model_name='participacion',
            name='tarea',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DjangoGePrApp.tarea'),
        ),
        migrations.CreateModel(
            name='Nota',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contenido', models.TextField()),
                ('fecha', models.DateField(auto_now_add=True)),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notas', to='DjangoGePrApp.empleado')),
                ('tarea', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notas', to='DjangoGePrApp.tarea')),
            ],
        ),
    ]

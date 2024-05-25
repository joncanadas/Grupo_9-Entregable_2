# Generated by Django 5.0.3 on 2024-05-25 11:10

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DjangoGePrApp', '0002_remove_tarea_empleados_delete_participacion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tarea',
            name='nivel_prioridad',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(3)]),
        ),
    ]

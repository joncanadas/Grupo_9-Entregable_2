# Generated by Django 5.0.3 on 2024-05-24 18:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('DjangoGePrApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tarea',
            name='empleados',
        ),
        migrations.DeleteModel(
            name='Participacion',
        ),
    ]

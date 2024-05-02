from django.db import models
from django.core.validators import MaxValueValidator


class Empleado(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    dni = models.CharField(max_length=20)
    telefono = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class Proyecto(models.Model):
    Nombre = models.CharField(max_length=30)
    Descripcion = models.CharField(max_length=300)
    Fecha_Inicio = models.DateField()
    Fecha_Fin = models.DateField()
    Presupuesto = models.IntegerField()


class Cliente(models.Model):
    Nombre = models.CharField(max_length=30)
    Telefono = models.IntegerField()
    Direccion = models.CharField(max_length=100)


class Tarea(models.Model):
    Nombre = models.CharField(max_length=30)
    Descripcion = models.CharField(max_length=300)
    Fecha_Inicio = models.DateField()
    Fecha_Fin = models.DateField()
    Nivel_Prioridad = models.CharField(
        max_length=10, choices=[("Alta", "Alta"), ("Media", "Media"), ("Baja", "Baja")]
    )
    Estado_Tarea = models.CharField(
        max_length=10,
        choices=[
            ("abierta", "Abierta"),
            ("asignada", "Asignada"),
            ("en_proceso", "En Proceso"),
            ("finalizada", "Finalizada"),
        ],
    )
    Notas = models.CharField(max_length=200)


class Participa(models.Model):
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE)
    tarea = models.ForeignKey(Tarea, on_delete=models.CASCADE)
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.empleado} participa en {self.proyecto} realizando {self.tarea}"


class Encarga(models.Model):
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    Num_Proyectos = models.IntegerField()


# class Empleado(models.Model):
#
#   tarea = models.ForeignKey(Tarea, on_delete=models.CASCADE)
#    DNI = models.CharField(max_length=9)
#    Nombre = models.CharField(max_length=20)
#    Apellido = models.CharField(max_length=20)
#    Telefono = models.IntegerField()
#    Email = models.CharField(max_length=30)
#
#    class Participa(models.Model):
#        proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE)
#        tarea = models.ForeignKey(Tarea, on_delete=models.CASCADE)
#        Empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
#        Horas = models.IntegerField()

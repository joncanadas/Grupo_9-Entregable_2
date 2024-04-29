from django.db import models 


class Proyecto(models.Model):
    Nombre = models.CharField(max_length=30)
    Descripcion = models.CharField(max_length=300)
    Fecha_Inicio = models.DateField()
    Fecha_Fin = models.DateField()
    Presupuesto = models.IntegerField()


class Cliente(models.Model):
     Nombre = models.CharField(max_length=30)
     Telefono = models.IntegerField(max_length=10)
     Direccion = Nombre = models.CharField(max_length=100)
    

class Encarga(models.Model):
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    Num_Proyectos = models.IntegerField()

class Tarea(models.Model):
    Nombre = models.CharField(max_length=30)
    Descripcion = models.CharField(max_length=300)
    Fecha_Inicio = models.DateField()
    Fecha_Fin = models.DateField()
    Nivel_Prioridad = models.IntegerField(max_number=3)
    Estado_Tarea = models.CharField(max_length=10)
    Notas = models.CharField(max_length=200)
    
class Empleado(models.Model):

 tarea = models.ForeignKey(Tarea, on_delete=models.CASCADE)
 DNI = models.CharField(max_length=9)
 Nombre = models.CharField(max_length=20)
 Apellido = models.CharField(max_length=20)
 Telefono = models.IntegerField()
 Email = models.CharField(max_length=30)
 
 class Participa(models.Model):
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE)
    tarea = models.ForeignKey(Tarea, on_delete=models.CASCADE)
    Empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    Horas = models.IntegerField()

    
    
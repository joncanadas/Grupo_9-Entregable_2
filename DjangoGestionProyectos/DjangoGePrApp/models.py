from django.db import models

# Create your models here.

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    direccion = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre

class Empleado(models.Model):
    dni = models.CharField(max_length=20, unique=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField()
    telefono = models.CharField(max_length=20)
    responsable = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.nombre} {self.apellido}'

class Proyecto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    presupuesto = models.DecimalField(max_digits=10, decimal_places=2)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='proyectos')

    def __str__(self):
        return self.nombre

class Tarea(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    nivel_prioridad = models.IntegerField()
    estado = models.CharField(max_length=50)
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE, related_name='tareas')
    responsable = models.ForeignKey(Empleado, on_delete=models.SET_NULL, null=True, related_name='tareas_responsables')
    empleados = models.ManyToManyField(Empleado, through='Participacion', related_name='tareas')

    def __str__(self):
        return self.nombre

class Participacion(models.Model):
    tarea = models.ForeignKey(Tarea, on_delete=models.CASCADE)
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    fecha_participacion = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.empleado} en {self.tarea}'

class Nota(models.Model):
    contenido = models.TextField()
    autor = models.ForeignKey(Empleado, on_delete=models.CASCADE, related_name='notas')
    fecha = models.DateField(auto_now_add=True)
    tarea = models.ForeignKey(Tarea, on_delete=models.CASCADE, related_name='notas')

    def __str__(self):
        return f'Nota de {self.autor} en {self.tarea}'

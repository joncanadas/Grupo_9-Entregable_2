from django.contrib import admin
from .models import Empleado, Proyecto, Tarea, Cliente, Nota, Participacion
 
# Register your models here.

admin.site.register(Empleado)
admin.site.register(Proyecto)
admin.site.register(Tarea)
admin.site.register(Cliente)
admin.site.register(Nota)
admin.site.register(Participacion)
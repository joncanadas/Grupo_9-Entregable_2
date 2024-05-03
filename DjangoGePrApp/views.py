from django.http import HttpResponse
from django.shortcuts import redirect
from django.shortcuts import render
from django.forms import modelform_factory
from .models import Proyecto, Tarea

# Create your views here.
def crearProyecto(request):
    proyectos = Proyecto.objects.all
    context = {'titulo_pagina' : 'Crear Proyectos', 'lista_proyectos' : proyectos}
    return render(request, 'crearProyecto.html', context)


def listados(request):
    proyectos = Proyecto.objects.all
    tareas = Tarea.objects.all
    context = {'titulo_pagina' : 'Listados de Proyectos y Tareas', 'lista_proyectos' : proyectos, 'lista_tareas' : tareas}
    return render(request, 'listados.html', context)

def modificar_Proyecto(request, proyecto_id):
    proyecto = Proyecto.objects.get(pk=proyecto_id)    

    Descripcion = request.POST["DescripcionProyectoMod"]
    Fecha_Inicio = request.POST["FechaInicioMod"]
    Fecha_Fin = request.POST["FechaFinMod"]
    Presupuesto = request.POST["PresupuestoMod"]
        
    context = {'titulo_pagina' : 'Modificar Proyectos', 'proyecto': proyecto}
    return render(request, 'modificarProyecto.html', context)

def crearTarea(request):
    tareas = Tarea.objects.all
    context = {'titulo_pagina' : 'Crear Tareas', 'lista_tareas' : tareas}
    return render(request, 'crearTarea.html', context)
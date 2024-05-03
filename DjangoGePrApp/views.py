from django.http import HttpResponse
from django.shortcuts import redirect
from django.shortcuts import render
from .forms import ProyectoForm
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

def modificarProyecto(request, proyecto_id):
    proyecto = Proyecto.objects.get(pk=proyecto_id)
    form = ProyectoForm()
    context = {'titulo_pagina' : 'Modificar Proyecto', 
               'proyecto' : proyecto, 'form' : form}
    return render(request, 'modificarProyecto.html', context)

def crearTarea(request):
    tareas = Tarea.objects.all
    context = {'titulo_pagina' : 'Crear Tareas', 'lista_tareas' : tareas}
    return render(request, 'crearTarea.html', context)

def borrarProyecto(request, proyecto_id):
    proyecto = Proyecto.objects.get(pk=proyecto_id)
    proyecto.delete()
    return redirect('listados')

def borrarTarea(request, tarea_id):
    proyecto = Tarea.objects.get(pk=tarea_id)
    proyecto.delete()
    return redirect('listados')
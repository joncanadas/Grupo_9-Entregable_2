from django.http import HttpResponse
from django.shortcuts import render
from .models import Proyecto, Tarea

# Create your views here.
def index(request):
    proyectos = Proyecto.objects.all
    context = {'titulo_pagina' : 'Crear Proyectos', 'lista_proyectos' : proyectos}
    return render(request, 'index.html', context)


def listarProyectos(request):
    proyectos = Proyecto.objects.all
    context = {'titulo_pagina' : 'Listado de Proyectos', 'lista_proyectos' : proyectos}
    return render(request, 'listarProyectos.html', context)

def modificarProyectos(request):
    proyectos = Proyecto.objects.all
    context = {'titulo_pagina' : 'Modificar Proyectos', 'lista_proyectos' : proyectos}
    return render(request, 'modificarProyecto.html', context)

def crearTarea(request):
    tareas = Tarea.objects.all
    context = {'titulo_pagina' : 'Crear Tareas', 'lista_tareas' : tareas}
    return render(request, 'crearTarea.html', context)
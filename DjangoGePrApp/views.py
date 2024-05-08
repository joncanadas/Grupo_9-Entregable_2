from django.http import HttpResponse
from django.shortcuts import redirect
from django.shortcuts import render
from .forms import ProyectoForm
from .models import Proyecto, Tarea
from .forms import ProyectoForm, TareaForm

# Create your views here.
def crearProyecto(request):
    form = ProyectoForm()
    if request.method == 'POST':
        form = ProyectoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listados')
    
    context = {'form': form}
    return render(request, 'crearProyecto.html', context)


def listados(request):
    proyectos = Proyecto.objects.all
    tareas = Tarea.objects.all
    context = {'titulo_pagina' : 'Listados de Proyectos y Tareas', 'lista_proyectos' : proyectos, 'lista_tareas' : tareas}
    return render(request, 'listados.html', context)


def modificarProyecto(request, proyecto_id):
    proyecto = Proyecto.objects.get(pk=proyecto_id)
    form = ProyectoForm(instance=proyecto)

    if request.method == 'POST':
        form = ProyectoForm(request.POST, instance=proyecto)
        if form.is_valid():
            form.save()
            return redirect('listados')

    context = {'titulo_pagina' : 'Modificar Proyecto', 
               'proyecto' : proyecto, 'form' : form}
    return render(request, 'modificarProyecto.html', context)


def modificarTarea(request, tarea_id):
    tarea = Tarea.objects.get(pk=tarea_id)
    form = TareaForm(instance=tarea)

    if request.method == 'POST':
        form = TareaForm(request.POST, instance=tarea)
        if form.is_valid():
            form.save()
            return redirect('listados')

    context = {'titulo_pagina' : 'Modificar Tarea', 
               'proyecto' : tarea, 'form' : form}
    return render(request, 'modificarTarea.html', context)


def crearTarea(request):
    form = TareaForm()
    if request.method == 'POST':
        form = TareaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listados')
    
    context = {'form': form}
    return render(request, 'crearTarea.html', context)


def borrarProyecto(request, proyecto_id):
    proyecto = Proyecto.objects.get(pk=proyecto_id)
    proyecto.delete()
    return redirect('listados')


def borrarTarea(request, tarea_id):
    proyecto = Tarea.objects.get(pk=tarea_id)
    proyecto.delete()
    return redirect('listados')
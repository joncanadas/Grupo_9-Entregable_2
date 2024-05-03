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

def modificarProyecto(request, proyecto_id):
    proyecto = Proyecto.objects.get(pk=proyecto_id)
    form_Proyecto = modelform_factory(Proyecto)
    
    if request.method == 'POST':
        form = form_Proyecto(request.POST, instance=proyecto)
        
        if form.is_valid():
            form.save()
            return redirect('detalle_proyecto', pk=proyecto.pk)
    else:
        form = modelform_factory(instance=proyecto)
        
    context = {'titulo_pagina' : 'Modificar Proyectos', 'form': form, 'proyecto': proyecto}
    return render(request, 'modificarProyecto.html', context)

def crearTarea(request):
    tareas = Tarea.objects.all
    context = {'titulo_pagina' : 'Crear Tareas', 'lista_tareas' : tareas}
    return render(request, 'crearTarea.html', context)

def borrarProyecto(request, proyecto_id):
    proyecto = Proyecto.objects.get(pk=proyecto_id)
    proyecto.delete()
    return redirect('listados')
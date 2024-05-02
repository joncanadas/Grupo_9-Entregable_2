from django.http import HttpResponse
from django.shortcuts import render
from .models import Proyecto

# Create your views here.
def index(request):
    proyectos = Proyecto.objects.all
    context = {'lista_proyectos' : proyectos}
    return render(request, 'index.html', context)


def listarProyectos(request):
    proyectos = Proyecto.objects.all
    context = {'titulo_pagina' : 'Listado de Proyectos', 'lista_poryectos' : proyectos}
    return render(request, 'listarProyectos.html', context)
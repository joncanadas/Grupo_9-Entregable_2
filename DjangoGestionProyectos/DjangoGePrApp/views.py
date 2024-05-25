from django.http import HttpResponse
from django.shortcuts import redirect
from django.shortcuts import render
from .forms import ProyectoForm
from .models import Proyecto, Tarea, Cliente, Empleado, Nota
from .forms import ProyectoForm, TareaForm, ClienteForm, EmpleadoForm, NotaForm


# Create your views here.
def listados(request):
    proyectos = Proyecto.objects.all
    tareas = Tarea.objects.all
    empleados = Empleado.objects.all
    clientes = Cliente.objects.all
    context = {
        "titulo_pagina": "Listados de Proyectos y Tareas",
        "lista_proyectos": proyectos,
        "lista_tareas": tareas,
        "lista_empleados": empleados,
        "lista_clientes": clientes,
    }
    return render(request, "listados.html", context)


def añadirCliente(request):
    form = ClienteForm()
    if request.method == "POST":
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("listados")

    context = {"titulo_pagina": "Añadir Cliente", "form": form}
    return render(request, "crearCliente.html", context)


def añadirEmpleado(request):
    form = EmpleadoForm()
    if request.method == "POST":
        form = EmpleadoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("listados")

    context = {"titulo_pagina": "Añadir Empleados", "form": form}
    return render(request, "crearEmpleado.html", context)


def añadirNota(request):
    form = NotaForm()
    if request.method == "POST":
        form = NotaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("listados")

    context = {"titulo_pagina": "Añadir Nota", "form": form}
    return render(request, "crearNotas.html", context)


def crearProyecto(request):
    form = ProyectoForm()
    if request.method == "POST":
        form = ProyectoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("listados")

    context = {"titulo_pagina": "Crear Proyecto", "form": form}
    return render(request, "crearProyecto.html", context)


def crearTarea(request):
    form = TareaForm()
    if request.method == "POST":
        form = TareaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("listados")

    context = {"titulo_pagina": "Crear Tarea", "form": form}
    return render(request, "crearTarea.html", context)


def modificarCliente(request, cliente_id):
    cliente = Cliente.objects.get(pk=cliente_id)
    form = ClienteForm(instance=cliente)

    if request.method == "POST":
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect("listados")

    context = {"titulo_pagina": "Modificar Cliente", "form": form}
    return render(request, "modificarCliente.html", context)


def modificarEmpleado(request, empleado_id):
    empleado = Empleado.objects.get(pk=empleado_id)
    form = EmpleadoForm(instance=empleado)

    if request.method == "POST":
        form = EmpleadoForm(request.POST, instance=empleado)
        if form.is_valid():
            form.save()
            return redirect("listados")

    context = {"titulo_pagina": "Modificar Empleado", "form": form}
    return render(request, "modificarEmpleado.html", context)


def modificarProyecto(request, proyecto_id):
    proyecto = Proyecto.objects.get(pk=proyecto_id)
    form = ProyectoForm(instance=proyecto)

    if request.method == "POST":
        form = ProyectoForm(request.POST, instance=proyecto)
        if form.is_valid():
            form.save()
            return redirect("listados")

    context = {"titulo_pagina": "Modificar Proyecto", "form": form}
    return render(request, "modificarProyecto.html", context)


def modificarTarea(request, tarea_id):
    tarea = Tarea.objects.get(pk=tarea_id)
    form = TareaForm(instance=tarea)

    if request.method == "POST":
        form = TareaForm(request.POST, instance=tarea)
        if form.is_valid():
            form.save()
            return redirect("listados")

    context = {"titulo_pagina": "Modificar Tarea", "form": form}
    return render(request, "modificarTarea.html", context)


def borrarCliente(request, cliente_id):
    cliente = Cliente.objects.get(pk=cliente_id)
    cliente.delete()
    return redirect("listados")


def borrarEmpleado(request, empleado_id):
    empleado = Empleado.objects.get(pk=empleado_id)
    empleado.delete()
    return redirect("listados")


def borrarProyecto(request, proyecto_id):
    proyecto = Proyecto.objects.get(pk=proyecto_id)
    proyecto.delete()
    return redirect("listados")


def borrarTarea(request, tarea_id):
    proyecto = Tarea.objects.get(pk=tarea_id)
    proyecto.delete()
    return redirect("listados")


def detProyecto(request, proyecto_id):
    proyecto = Proyecto.objects.get(pk=proyecto_id)
    context = {"titulo_pagina": "Proyecto Detallado", "pro": proyecto}
    return render(request, "detProyecto.html", context)


def detTarea(request, tarea_id):
    tarea = Tarea.objects.get(pk=tarea_id)
    notas = Nota.objects.filter(tarea=tarea)
    context = {"titulo_pagina": "Tarea Detallada", "tar": tarea, "notas": notas}
    return render(request, "detTarea.html", context)


def detEmpleado(request, empleado_id):
    empleado = Empleado.objects.get(pk=empleado_id)
    context = {"titulo_pagina": "Empleado Detallado", "emp": empleado}
    return render(request, "detEmpleado.html", context)


def detCliente(request, cliente_id):
    cliente = Cliente.objects.get(pk=cliente_id)
    context = {"titulo_pagina": "Cliente Detallado", "cli": cliente}
    return render(request, "detCliente.html", context)

from django.http import HttpResponse
from django.shortcuts import redirect
from django.shortcuts import render
from django.core.mail import send_mail
from .forms import ProyectoForm
from .models import Proyecto, Tarea, Cliente, Empleado, Nota
from .forms import ProyectoForm, TareaForm, ClienteForm, EmpleadoForm, NotaForm, EmailForm


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

def enviarCorreo(request):
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            subject = 'Información sobre Deustronic Components S.L.'
            message = (
                'Estimado/a,\n\n'
                'Nos complace informarle sobre Deustronic Components S.L., una compañía líder en la gestión de proyectos industriales. '
                'Nuestro compromiso es proporcionar soluciones innovadoras y eficientes que satisfagan las necesidades específicas '
                'de nuestros clientes en el sector industrial.\n\n'
                '¿Quiénes somos?\n\n'
                'Deustronic Components S.L. se especializa en la planificación, ejecución y supervisión de proyectos industriales de diversa '
                'envergadura. Contamos con un equipo de profesionales altamente cualificados y con amplia experiencia en el sector, lo que '
                'nos permite ofrecer servicios de calidad y garantizar el éxito de cada proyecto.\n\n'
                'Nuestros Servicios\n\n'
                'Entre los servicios que ofrecemos se encuentran:\n'
                '- Consultoría y planificación de proyectos: Asesoramiento experto para la definición y organización de sus proyectos industriales.\n'
                '- Ingeniería y diseño: Desarrollo de soluciones técnicas personalizadas que cumplen con los más altos estándares de calidad y eficiencia.\n'
                '- Gestión de la construcción: Supervisión integral de la ejecución de obras, asegurando el cumplimiento de plazos y presupuestos.\n'
                '- Mantenimiento y soporte: Servicios de mantenimiento preventivo y correctivo para asegurar la operatividad continua de sus instalaciones.\n\n'
                'Nuestro Compromiso\n\n'
                'En Deustronic Components S.L., nos comprometemos a:\n'
                '- Brindar soluciones personalizadas que se adapten a las necesidades específicas de cada cliente.\n'
                '- Utilizar tecnologías de vanguardia y prácticas sostenibles en todos nuestros proyectos.\n'
                '- Garantizar la seguridad y el bienestar de nuestro equipo y de todas las partes involucradas en nuestros proyectos.\n\n'
                'Contáctenos\n\n'
                'Si desea obtener más información sobre nuestros servicios o tiene alguna consulta, no dude en ponerse en contacto con nosotros. '
                'Puede responder a este correo electrónico o llamarnos al 674231938.'
                'para conocer más sobre nuestro trabajo.\n\n'
                'Agradecemos su interés en Deustronic Components S.L. y esperamos poder colaborar con usted en futuros proyectos.\n\n'
                'Atentamente,\n\n'
                'Mikel García García\n'
                'Desarrollador SW\n'
                'Deustronic Components S.L.\n'
                'grupo9ingweb@gmail.com\n'
                '674231938\n'      
            )
            send_mail(
                subject,
                message,
                'tucorreo@gmail.com',  # Reemplaza con tu correo
                [email],
                fail_silently=False,
            )
            return render(request, 'correoEnviado.html')
    else:
        form = EmailForm()

    return render(request, 'enviarCorreo.html', {'form': form})
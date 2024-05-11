from django.urls import path
from . import views

urlpatterns = [
    path('listados/', views.listados, name='listados'),
    path('crearProyecto/', views.crearProyecto, name='crearProyecto'),
    path('crearTarea/', views.crearTarea, name='crearTareas'),
    path('añadirEmpleado/', views.añadirEmpleado, name='añadirEmpleado'),
    path('añadirCliente/', views.añadirCliente, name='añadirCliente'),
    path('modificarProyecto/<int:proyecto_id>/', views.modificarProyecto, name='modificarProyecto'),
    path('modificarTarea/<int:tarea_id>/', views.modificarTarea, name='modificarTarea'),
    path('modificarEmpleado/<int:empleado_id>/', views.modificarEmpleado, name='modificarEmpleado'),
    path('modificarCliente/<int:cliente_id>/', views.modificarCliente, name='modificarCliente'),
    path('proyecto/delete/<int:proyecto_id>/', views.borrarProyecto, name='borrarProyecto'),
    path('tarea/delete/<int:tarea_id>/', views.borrarTarea, name='borrarTarea'),
    path('empleado/delete/<int:empleado_id>/', views.borrarEmpleado, name='borrarEmpleado'),
    path('cliente/delete/<int:cliente_id>/', views.borrarCliente, name='borrarCliente'),
]
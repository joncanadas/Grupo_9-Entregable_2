from django.urls import path
from . import views

urlpatterns = [
    path('listados/', views.listados, name='listados'),
    path('crearProyecto/', views.crearProyecto, name='crearProyecto'),
    path('crearTarea/', views.crearTarea, name='crearTareas'),
    path('añadirNota/', views.añadirNota, name='añadirNota'),
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
    path('detProyecto/<int:proyecto_id>/', views.detProyecto, name='detProyecto'),
    path('detTarea/<int:tarea_id>/', views.detTarea, name='detTarea'),
    path('detEmpleado/<int:empleado_id>/', views.detEmpleado, name='detEmpleado'),
    path('detCliente/<int:cliente_id>/', views.detCliente, name='detCliente'),
    path('enviarCorreo/', views.enviarCorreo, name='enviarCorreo'),
    path('login/', views.login, name='login'),
    path('registro/', views.registro, name='registro'),
    path('logout/', views.logout, name='logout'),
    path('api/proyecto/<int:proyecto_id>/', views.proyecto_api, name='proyecto_api')

]
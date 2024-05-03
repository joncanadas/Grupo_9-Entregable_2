from django.urls import path
from . import views
from .views import ProyectoUpdateView

urlpatterns = [
    path('crearProyecto/', views.crearProyecto, name='crearProyecto'),
    path('listados/', views.listados, name='listados'),
    path('modificarProyecto/<int:proyecto_id>/', ProyectoUpdateView.as_view(), name='modificarProyecto'),
    path('crearTarea/', views.crearTarea, name='crearTareas'),
    path('proyecto/delete/<int:proyecto_id>/', views.borrarProyecto, name='borrarProyecto'),
    path('tarea/delete/<int:tarea_id>/', views.borrarTarea, name='borrarTarea'),

]
from django.urls import path
from . import views

urlpatterns = [
    path('crearProyecto/', views.crearProyecto, name='crearProyecto'),
    path('listados/', views.listados, name='listados'),
    path('modificarProyecto/<int:proyecto_id>/', views.modificar_Proyecto, name='modificarProyecto'),
    path('crearTarea/', views.crearTarea, name='crearTareas'),
]
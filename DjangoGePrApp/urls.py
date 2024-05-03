from django.urls import path
from . import views

urlpatterns = [
    path('crearProyecto/', views.crearProyecto, name='crearProyecto'),
    path('listados/', views.listados, name='listados'),
    path('modificarProyecto/', views.modificarProyectos, name='modificarProyectos'),
    path('crearTarea/', views.crearTarea, name='crearTareas'),
]
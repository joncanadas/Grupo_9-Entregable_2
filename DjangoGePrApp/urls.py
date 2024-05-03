from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('listarProyecto/', views.listarProyectos, name='listarProyectos'),
    path('modificarProyecto/', views.modificarProyectos, name='modificarProyectos'),
    path('crearTarea/', views.crearTarea, name='crearTareas'),
]
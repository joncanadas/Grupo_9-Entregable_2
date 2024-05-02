from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('listarProyecto/', views.listadoProyectos, name='listadoProyectos'),
]
from django import forms
from DjangoGePrApp.models import Proyecto, Tarea


class ProyectoForm(forms.Form):
    Nombre = forms.CharField(label="Nombre", max_length=100)
    Descripcion = forms.CharField(label="Descripcion", max_length=300)
    Fecha_Inicio = forms.DateField(label="Fecha_Inicio")
    Fecha_Fin = forms.DateField(label="Fecha_Fin")
    Presupuesto = forms.IntegerField(label="Presupuesto")

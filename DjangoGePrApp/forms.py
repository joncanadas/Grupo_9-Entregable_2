<<<<<<< HEAD
from django.forms import ModelForm
from .models import Proyecto, Tarea

class ProyectoForm(ModelForm):
    class Meta:
        model = Proyecto
        fields = '__all__'
        
class TareaForm(ModelForm):
    class Meta:
        model = Tarea
        fields = '__all__'
=======
from django import forms
from DjangoGePrApp.models import Proyecto, Tarea


class ProyectoForm(forms.Form):
    Nombre = forms.CharField(label="Nombre", max_length=100)
    Descripcion = forms.CharField(label="Descripcion", max_length=300)
    Fecha_Inicio = forms.DateField(label="Fecha_Inicio")
    Fecha_Fin = forms.DateField(label="Fecha_Fin")
    Presupuesto = forms.IntegerField(label="Presupuesto")
>>>>>>> cd34b82c221bfcacbaa77beb733ef12fbbff4334

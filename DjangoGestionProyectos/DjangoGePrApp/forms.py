from django import forms
from django.forms import ModelForm
from .models import Proyecto, Tarea, Empleado, Cliente

class ProyectoForm(ModelForm):
    class Meta:
        model = Proyecto
        fields = '__all__'
        widgets = {
            'fecha_inicio': forms.DateInput(attrs={'type': 'date'}),
            'fecha_fin': forms.DateInput(attrs={'type': 'date'}),
        }
        
class TareaForm(ModelForm):
    class Meta:
        model = Tarea
        fields = '__all__'
        
class EmpleadoForm(ModelForm):
    class Meta:
        model = Empleado
        fields = '__all__'
        
class ClienteForm(ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'
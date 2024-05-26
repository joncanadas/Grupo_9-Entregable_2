from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm 
from django.contrib.auth.models import User
from django.forms.widgets import PasswordInput, TextInput
from django.forms import ModelForm
from .models import Proyecto, Tarea, Empleado, Cliente, Nota


class ProyectoForm(ModelForm):
    class Meta:
        model = Proyecto
        fields = "__all__"
        widgets = {
            "fecha_inicio": forms.DateInput(attrs={"type": "date"}),
            "fecha_fin": forms.DateInput(attrs={"type": "date"}),
        }


class TareaForm(ModelForm):
    class Meta:
        model = Tarea
        fields = "__all__"
        widgets = {
            "fecha_inicio": forms.DateInput(attrs={"type": "date"}),
            "fecha_fin": forms.DateInput(attrs={"type": "date"}),
        }


class NotaForm(ModelForm):
    class Meta:
        model = Nota
        fields = "__all__"


class EmpleadoForm(ModelForm):
    class Meta:
        model = Empleado
        fields = "__all__"


class ClienteForm(ModelForm):
    class Meta:
        model = Cliente
        fields = "__all__"


class EmailForm(forms.Form):
    email = forms.EmailField(label='Tu correo electrónico', max_length=100)
    

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        

class LoginForm(AuthenticationForm):
    
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())
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
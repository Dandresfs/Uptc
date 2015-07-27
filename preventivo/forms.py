from django.forms import ModelForm
from .models import Actividades

class NuevaActividad(ModelForm):
    class Meta:
        model = Actividades
        exclude = ['maquina']
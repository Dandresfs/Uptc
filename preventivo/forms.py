from django.forms import ModelForm
from .models import Actividades, TipoMantenimiento

class NuevaActividad(ModelForm):
    class Meta:
        model = Actividades
        exclude = ['maquina','tipo']

class PlanMantenimiento(ModelForm):
    class Meta:
        model = TipoMantenimiento
        exclude = ['nombre']
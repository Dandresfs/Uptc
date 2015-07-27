from django.forms import ModelForm
from django.forms.widgets import TextInput,Textarea
from .models import InventarioEquipos

class NuevoInventarioEquipos(ModelForm):
    class Meta:
        model = InventarioEquipos
        widgets={
            'descripcion':Textarea({'rows':'4'}),
            'color':TextInput(attrs={'type':'color','value':"#ff0000"})
        }
        fields = ['nombre','descripcion','color','imagen','pdf']
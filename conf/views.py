from django.views.generic import TemplateView

class Inicio(TemplateView):
    template_name = 'inicio.html'

class Ubicacion(TemplateView):
    template_name = 'ubicacion.html'

class Mantenimiento(TemplateView):
    template_name = 'mantenimiento.html'
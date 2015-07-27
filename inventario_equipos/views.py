from django.views.generic.edit import FormView,UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic import TemplateView

from .forms import NuevoInventarioEquipos
from .models import InventarioEquipos
from preventivo.models import EventCalendar

class InventarioView(ListView):
    model = InventarioEquipos
    template_name = 'inventario_equipos.html'

    def get_context_data(self, **kwargs):
        return super(InventarioView,self).get_context_data(**kwargs)

class InventarioUpdateView(UpdateView):
    template_name = 'nuevo_inventario_equipos.html'
    model = InventarioEquipos
    form_class = NuevoInventarioEquipos
    success_url = '/inventario'

    def form_valid(self, form):
        self.object = form.save()
        events = EventCalendar.objects.all().filter(maquina__id=self.kwargs['pk'])
        for event in events:
            event.color = form.cleaned_data['color']
            event.save()
        return super(InventarioUpdateView,self).form_valid(form)

class InventarioDeleteView(DeleteView):
    template_name = 'eliminar.html'
    model = InventarioEquipos
    success_url = '/inventario'

class NuevoInventarioEquiposForm(FormView):
    template_name = 'nuevo_inventario_equipos.html'
    form_class = NuevoInventarioEquipos
    success_url = '/inventario'

    def form_valid(self, form):
        form.save()
        return super(NuevoInventarioEquiposForm, self).form_valid(form)

class CalendarioMaquinaView(TemplateView):
    template_name = 'calendario_maquina.html'

    def get_context_data(self, **kwargs):
        kwargs['maquina'] = self.kwargs['idmachine']
        kwargs['nombre'] = InventarioEquipos.objects.get(id=self.kwargs['idmachine']).nombre
        return super(CalendarioMaquinaView,self).get_context_data(**kwargs)

class CalendarioFullView(TemplateView):
    template_name = 'calendario_total.html'
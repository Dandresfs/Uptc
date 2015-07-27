from django.views.generic.list import ListView
from django.views.generic.edit import FormView
from .forms import NuevaActividad
from .models import Actividades
from inventario_equipos.models import InventarioEquipos
from .serializers import EventSerializer, EventFullSerializer, ActividadSerializer
from .models import EventCalendar,TipoMantenimiento
from django.views.generic.edit import DeleteView, UpdateView

class ActividadView(ListView):
    model = Actividades
    template_name = "lista_actividades.html"

    def get_queryset(self):
        queryset = Actividades.objects.all().filter(maquina__id=self.kwargs['idmachine'])
        return queryset

    def get_context_data(self, **kwargs):
        kwargs['nombremaquina'] = InventarioEquipos.objects.get(id=self.kwargs['idmachine']).nombre
        return super(ActividadView,self).get_context_data(**kwargs)

class ActividadEditarView(ListView):
    model = Actividades
    template_name = "lista_actividades_editar.html"

    def get_queryset(self):
        queryset = Actividades.objects.all().filter(maquina__id=self.kwargs['idmachine'])
        return queryset

    def get_context_data(self, **kwargs):
        kwargs['nombremaquina'] = InventarioEquipos.objects.get(id=self.kwargs['idmachine']).nombre
        return super(ActividadEditarView,self).get_context_data(**kwargs)

class InventarioView(ListView):
    model = InventarioEquipos
    template_name = 'lista_maquinas.html'

    def get_context_data(self, **kwargs):
        kwargs['nombremantenimiento'] = TipoMantenimiento.objects.get(id=self.kwargs['idmantenimiento']).nombre
        return super(InventarioView,self).get_context_data(**kwargs)

class NuevaActividadForm(FormView):
    template_name = 'nueva_actividad.html'
    form_class = NuevaActividad
    success_url = '../'

    def form_valid(self, form):
        form.instance.maquina = InventarioEquipos.objects.get(pk = self.kwargs['idmachine'])
        form.save()
        return super(NuevaActividadForm, self).form_valid(form)

class ActividadDeleteView(DeleteView):
    template_name = 'eliminar_actividad.html'
    model = Actividades
    success_url = '../../'

class ActividadUpdateView(UpdateView):
    template_name = 'nueva_actividad.html'
    model = Actividades
    form_class = NuevaActividad
    success_url = '../../'

class CalendarioView(ListView):
    model = Actividades
    template_name = 'calendario.html'

    def get_queryset(self):
        queryset = Actividades.objects.all().filter(maquina__id=self.kwargs['idmachine'])
        return queryset

    def get_context_data(self, **kwargs):
        kwargs['color'] = InventarioEquipos.objects.all().filter(id=self.kwargs['idmachine'])[0].color
        kwargs['mantenimiento'] = self.kwargs['idmantenimiento']
        kwargs['nombremantenimiento'] = TipoMantenimiento.objects.get(id=self.kwargs['idmantenimiento']).nombre
        kwargs['maquina'] = self.kwargs['idmachine']
        kwargs['nombremaquina'] = InventarioEquipos.objects.get(id=self.kwargs['idmachine']).nombre
        return super(CalendarioView,self).get_context_data(**kwargs)

from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from django.http import Http404
from rest_framework.permissions import IsAuthenticated

class EventList(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, maquina, mantenimiento, format=None):
        snippet = EventCalendar.objects.all().filter(mantenimiento__id=mantenimiento).filter(maquina__id=maquina)
        serializer = EventSerializer(snippet,many=True)
        return Response(serializer.data)

    def post(self, request, maquina, mantenimiento, format=None):
        serializer = EventFullSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EventDetail(APIView):

    permission_classes = (IsAuthenticated,)

    def get_object(self, pk):
        try:
            return EventCalendar.objects.get(pk=pk)
        except EventCalendar.DoesNotExist:
            raise Http404

    def get(self, request, pk, maquina, mantenimiento, format=None):
        snippet = self.get_object(pk)
        serializer = EventSerializer(snippet)
        return Response(serializer.data)


    def put(self, request, pk, maquina, mantenimiento ,format=None):
        snippet = self.get_object(pk)
        serializer = EventSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, maquina, mantenimiento, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class EventListMachine(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, maquina, format=None):
        snippet = EventCalendar.objects.all().filter(maquina__id=maquina)
        serializer = EventSerializer(snippet,many=True)
        return Response(serializer.data)

class EventListFull(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        snippet = EventCalendar.objects.all()
        serializer = EventSerializer(snippet,many=True)
        return Response(serializer.data)

class ActividadList(APIView):
    permission_classes = (IsAuthenticated,)



    def get(self, request, nombre, format=None):
        snippet = Actividades.objects.all().filter(nombre=nombre)
        serializer = ActividadSerializer(snippet,many=True)
        return Response(serializer.data)
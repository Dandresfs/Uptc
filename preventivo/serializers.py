from rest_framework import serializers
from .models import EventCalendar,Actividades

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventCalendar
        fields = ('id','title','start','end','color','icono')

class EventFullSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventCalendar
        fields = ('id','title','start','end','color','icono','mantenimiento','maquina')

class ActividadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actividades
        fields = ('nombre','descripcion','imagen')
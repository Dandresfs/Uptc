from django.contrib import admin
from .models import Actividades, EventCalendar, TipoMantenimiento

admin.site.register(Actividades)
admin.site.register(EventCalendar)
admin.site.register(TipoMantenimiento)
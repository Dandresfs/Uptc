from django.conf.urls import url
from .views import InventarioView,NuevoInventarioEquiposForm,InventarioUpdateView,InventarioDeleteView, CalendarioMaquinaView
from .views import CalendarioFullView
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^$',login_required(InventarioView.as_view()),name="inventario_equipos"),
    url(r'^nuevo/$',login_required(NuevoInventarioEquiposForm.as_view()),name="nuevo_inventario_equipos"),
    url(r'^(?P<pk>\w+)/editar/$',login_required(InventarioUpdateView.as_view())),
    url(r'^(?P<pk>\w+)/eliminar/$',login_required(InventarioDeleteView.as_view())),
    url(r'^(?P<idmachine>\w+)/calendario/$',login_required(CalendarioMaquinaView.as_view())),
    url(r'^calendario/$',login_required(CalendarioFullView.as_view())),
]
"""untitled URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from .views import Inicio,Ubicacion, Mantenimiento
from django.contrib import admin
from django.conf import settings
from django.contrib.auth.decorators import login_required
from .views import GrupoView

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$','django.contrib.auth.views.login',{'template_name':'login.html'}, name='login'),
    url(r'^cerrar/$','django.contrib.auth.views.logout_then_login',name='logout'),
    url(r'^inicio/$',Inicio.as_view(),name="inicio"),
    url(r'^ubicacion/$',login_required(Ubicacion.as_view()),name="ubicacion"),
    url(r'^mantenimiento/$',login_required(Mantenimiento.as_view()),name="mantenimiento"),
    url(r'^inventario/',include('inventario_equipos.urls')),
    url(r'^tipo/',include('preventivo.urls')),
    url(r'^grupo/$',login_required(GrupoView.as_view())),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',{'document_root': settings.MEDIA_ROOT,}),
]
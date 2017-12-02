"""Gestion_Academica URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth.views import login,logout_then_login

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [

    url(r'^admin/', admin.site.urls,name="root"),
    url(r'^persona/', include('app.persona.urls', namespace="persona")),
    url(r'^gestionareas/', include('app.areadeinvestigacion.urls', namespace="gruposinvestigacion")),
    url(r'^proyecto/', include('app.proyecto.urls', namespace="proyecto")),
    url(r'^usuario/', include('app.usuario.urls', namespace="usuario")),
    url(r'^accounts/login/', login, {'template_name': 'index.html'}, name='login'),
    url(r'^$', login, {'template_name': 'index.html'}, name='login'),
    url(r'^logout/', logout_then_login, name='logout'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
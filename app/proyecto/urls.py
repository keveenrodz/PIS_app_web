from django.conf.urls import url, include
from app.proyecto.views import ProyectoCreate, ProyectoUpdate\
    ,ProyectoUpdate2,ProyectoUpdate3, ProyectoDelete, post_listar,post_listarasignados,post_misproyectos,ReporteProyectoExcel
from django.contrib.auth.decorators import login_required

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
######### URLS DE MANEJO DE PROYECTOS ########
    url(r'^nuevo/$',  login_required(ProyectoCreate.as_view()), name='proyecto_crear'),
    url(r'^listar/$', login_required(post_listar), name='proyecto_listar'),
    url(r'^listarproyectosasignados/$', login_required(post_listarasignados), name='proyecto_listarasginados'),
    url(r'^listarmisproyectos/$', login_required(post_misproyectos), name='proyecto_listarmisproyectos'),
    url(r'^editar/(?P<pk>\d+)/$', login_required(ProyectoUpdate.as_view()), name='proyecto_editar'),
    url(r'^editar2/(?P<pk>\d+)/$', login_required(ProyectoUpdate2.as_view()), name='proyecto_editar2'),
    url(r'^editar3/(?P<pk>\d+)/$', login_required(ProyectoUpdate3.as_view()), name='proyecto_editar3'),
    url(r'^eliminar/(?P<pk>\d+)/$', login_required(ProyectoDelete.as_view()), name='proyecto_eliminar'),
    url(r'^reporte_proyecto_excel$',login_required(ReporteProyectoExcel.as_view()), name="reporte_proyecto_excel"),
]

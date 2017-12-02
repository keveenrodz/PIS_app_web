from django.conf.urls import url, include
from django.contrib.auth.decorators import login_required
from app.persona.views import EstudianteList, EstudianteCreate, EstudianteUpdate, EstudianteDelete,  \
    AsesorList, AsesorCreate, AsesorUpdate, AsesorDelete, DirectivoList, DirectivoCreate, DirectivoUpdate, DirectivoDelete,\
    ReporteEstudiantesExcel, DirectivoVista




urlpatterns = [
######### URLS DE MANEJO DE ESTUDIANTES ########
    url(r'^estudiante/nuevo$',  login_required(EstudianteCreate.as_view()), name='estudiante_crear'),
    url(r'^estudiante/listar$', login_required(EstudianteList.as_view()), name='estudiante_listar'),
    url(r'^estudiante/editar/(?P<pk>\d+)/$', login_required(EstudianteUpdate.as_view()), name='estudiante_editar'),
    url(r'^estudiante/eliminar/(?P<pk>\d+)/$', login_required(EstudianteDelete.as_view()), name='estudiante_eliminar'),
    url(r'^reporte_estudiante_excel$',login_required(ReporteEstudiantesExcel.as_view()), name="reporte_estudiante_excel"),
######### URLS DE MANEJO DE ASESORES ########
    url(r'^asesor/nuevo$',  login_required(AsesorCreate.as_view()), name='asesor_crear'),
    url(r'^asesor/listar$', login_required(AsesorList.as_view()), name='asesor_listar'),
    url(r'^asesor/editar/(?P<pk>\d+)/$', login_required(AsesorUpdate.as_view()), name='asesor_editar'),
    url(r'^asesor/eliminar/(?P<pk>\d+)/$', login_required(AsesorDelete.as_view()), name='asesor_eliminar'),
######### URLS DE MANEJO DE DIRECTIVOS ########
    url(r'^directivo/nuevo$',  login_required(DirectivoCreate.as_view()), name='directivo_crear'),
    url(r'^directivo/listar$', login_required(DirectivoList.as_view()), name='directivo_listar'),
    url(r'^directivo/editar/(?P<pk>\d+)/$', login_required(DirectivoUpdate.as_view()), name='directivo_editar'),
    url(r'^directivo/eliminar/(?P<pk>\d+)/$', login_required(DirectivoDelete.as_view()), name='directivo_eliminar'),
    url(r'^directivo/vista$', login_required(DirectivoVista.as_view()), name='home_directivo'),
]

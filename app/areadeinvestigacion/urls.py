from django.conf.urls import url, include
from app.areadeinvestigacion.views import AreaList, AreaCreate, AreaUpdate, AreaDelete, \
    GrupoList, GrupoCreate, GrupoUpdate, GrupoDelete
from django.contrib.auth.decorators import login_required


urlpatterns = [
    ######### URLS DE MANEJO DE ÁREA ########
    url(r'^area/listar$', login_required(AreaList.as_view()), name='area_listar'),
    url(r'^area/nueva$', login_required(AreaCreate.as_view()), name='area_crear'),
    url(r'^area/editar/(?P<pk>\d+)$', login_required(AreaUpdate.as_view()), name='area_editar'),
    url(r'^area/eliminar/(?P<pk>\d+)$', login_required(AreaDelete.as_view()), name='area_eliminar'),

    ######### URLS DE MANEJO DE GRUPOS DE INVESTIGACION ########
    url(r'^grupo/listar$', login_required(GrupoList.as_view()), name='grupoinv_listar'),
    url(r'^grupo/nueva$', login_required(GrupoCreate.as_view()), name='grupoinv_crear'),
    url(r'^grupo/editar/(?P<pk>\d+)$', login_required(GrupoUpdate.as_view()), name='grupoinv_editar'),
    url(r'^grupo/eliminar/(?P<pk>\d+)$', login_required(GrupoDelete.as_view()), name='grupoinv_eliminar'),

]
from django.conf.urls import url
from app.usuario.views import RegistroUsuario, RegistroList, RegistroUpdate,RegistroDelete,ValidarLogin
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^registrar$', RegistroUsuario.as_view(), name="registrar"),
    url(r'^listar$', login_required(RegistroList.as_view()), name='usuario_listar'),
    url(r'^editar/(?P<pk>\d+)/$', login_required(RegistroUpdate.as_view()), name='usuario_editar'),
    url(r'^eliminar/(?P<pk>\d+)/$', login_required(RegistroDelete.as_view()), name='usuario_eliminar'),
    url(r'^validar$', ValidarLogin, name="usuario_validar"),
]
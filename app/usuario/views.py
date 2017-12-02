from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from app.usuario.forms import RegistroForm
from app.persona.models import Persona
from app.proyecto.models import ProyectoGrado
from django.http.response import HttpResponseRedirect
# Create your views here.

class RegistroList(ListView):
    model = User
    template_name = 'usuario/usuario_list.html'

class RegistroUsuario(CreateView):
    model = User
    template_name = "usuario/registrar.html"
    form_class = RegistroForm
    success_url = reverse_lazy('login')

class RegistroUpdate(UpdateView):
    model = User
    form_class = RegistroForm
    template_name = "usuario/usuario_form.html"
    success_url = reverse_lazy('usuario:usuario_listar')

class RegistroDelete(DeleteView):
    model = User
    template_name = 'usuario/usuario_delete.html'
    success_url = reverse_lazy('usuario:usuario_listar')

def ValidarLogin(request):
    if request.user.is_superuser == True:
        return HttpResponseRedirect('/admin') ##REDIRECCIONAR A ALGUNA PAGINA DEL PROGRAMA O AL ADMIN DJANGO
    else:
        tipo = (Persona.objects.get(usuario_id=request.user.id)).tipo_usuario
        if tipo == 'Estudiante':
            return redirect('proyecto:proyecto_listarmisproyectos')
        elif tipo == 'Asesor':
            return redirect('proyecto:proyecto_listarasginados')
        elif tipo == 'Directivo':
            return redirect('persona:home_directivo')

from django.shortcuts import render
from app.areadeinvestigacion.forms import AreaForm, GruposInvForm
from app.areadeinvestigacion.models import area, GrupoInvestigacion
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
# Create your views here.

################################################
############## CLASES DE GESTION ÄREA LISAR, EDITAR, ELIMINAR Y BORRAR ###############
class AreaList(ListView):
    model = area
    template_name = 'areadeinvestigacion/area_list.html'

class AreaCreate(CreateView):
    model = area
    form_class = AreaForm
    template_name = 'areadeinvestigacion/area_form.html'
    success_url = reverse_lazy('gruposinvestigacion:area_listar')

class AreaUpdate(UpdateView):
    model = area
    form_class = AreaForm
    template_name = 'areadeinvestigacion/area_form.html'
    success_url = reverse_lazy('gruposinvestigacion:area_listar')

class AreaDelete(DeleteView):
    model = area
    template_name = 'areadeinvestigacion/area_delete.html'
    success_url = reverse_lazy('gruposinvestigacion:area_listar')

################################################
############## CLASES DE GESTION GRUPO DE INVESTIGACION LISAR, EDITAR, ELIMINAR Y BORRAR ###############

class GrupoList(ListView):
    model = GrupoInvestigacion
    template_name = 'areadeinvestigacion/grupoinv_list.html'

class GrupoCreate(CreateView):
    model = GrupoInvestigacion
    form_class = GruposInvForm
    template_name = 'areadeinvestigacion/grupoinv_form.html'
    success_url = reverse_lazy('gruposinvestigacion:grupoinv_listar')

class GrupoUpdate(UpdateView):
    model = GrupoInvestigacion
    form_class = GruposInvForm
    template_name = 'areadeinvestigacion/grupoinv_form.html'
    success_url = reverse_lazy('gruposinvestigacion:grupoinv_listar')

class GrupoDelete(DeleteView):
    model = GrupoInvestigacion
    template_name = 'areadeinvestigacion/grupoinv_delete.html'
    success_url = reverse_lazy('gruposinvestigacion:grupoinv_listar')
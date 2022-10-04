from django.shortcuts import render, redirect
from django.views.generic import CreateView, DeleteView, ListView, UpdateView
from django.urls import reverse_lazy
from .forms import ModalidadForm, caratulaForm
from .models import Modalidad, caratula

# =========================================================================
# =========================================================================
# Modalidad de violencia
class ModalidadList(ListView):
    model = Modalidad
    template_name = 'index.html'

class ModalidadCreate(CreateView):
    model = Modalidad
    form_class = ModalidadForm
    template_name = 'agregar_modalidad.html'
    success_url = reverse_lazy('index')

class ModalidadUpdate(UpdateView):
    model = Modalidad
    form_class = ModalidadForm
    template_name = 'agregar_modalidad.html'
    success_url = reverse_lazy('index')

class ModalidadDelete(DeleteView):
    model = Modalidad
    template_name = 'verificacion.html'
    success_url = reverse_lazy('index')
# =========================================================================
# =========================================================================
class caratulaList(ListView):
    model = caratula
    template_name = 'index.html'

class caratulaCreate(CreateView):
    model = caratula
    form_class = caratulaForm
    template_name = 'agregar_modalidad.html'
    success_url = reverse_lazy('index')

class caratulaUpdate(UpdateView):
    model = caratula
    form_class = caratulaForm
    template_name = 'agregar_modalidad.html'
    success_url = reverse_lazy('index')

class caratulaDelete(DeleteView):
    model = caratula
    template_name = 'verificacion.html'
    success_url = reverse_lazy('index')
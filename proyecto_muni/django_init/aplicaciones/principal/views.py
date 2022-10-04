from django.shortcuts import render, redirect
from .models import *
from .forms import *

# Create your views here.

def inicio(request): 
    modalidad = Modalidad.objects.all()
    contexto = {
        'modalidad':modalidad
    }
    return render(request, 'index.html',contexto)

def agregarModalidad(request):
    if request.method == 'GET':
        form = ModalidadForm()
        contexto = {
        'form':form
    }
    else:
        form = ModalidadForm(request.POST)
        contexto = {
        'form':form
    }
    if form.is_valid():
        form.save()
        return redirect('index')
    return render(request,'agregar_modalidad.html',contexto)

def editarModalidad(request,id):
    modalidad = Modalidad.objects.get(id = id)
    if request.method == 'GET':
        form = ModalidadForm(instance= modalidad)
        contexto = {
        'form':form
    }
    else:
        form = ModalidadForm(request.POST, instance= modalidad)
        contexto = {
        'form':form
    }
        if form.is_valid():
            form.save()
            return redirect('index')
    return render(request,'agregar_modalidad.html',contexto)

def eliminarModalidad(request,id):
    modalidad = Modalidad.objects.get(id = id)
    modalidad.delete()
    return redirect('index')

# ========================================================

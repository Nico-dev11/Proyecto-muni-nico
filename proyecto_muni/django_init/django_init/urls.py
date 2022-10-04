"""django_init URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from unicodedata import name
from django.contrib import admin
from django.urls import path
# from aplicaciones.principal.views import inicio,agregarModalidad,editarModalidad,eliminarModalidad
from aplicaciones.principal.class_view import ModalidadList, ModalidadCreate, ModalidadUpdate, ModalidadDelete, caratulaList, caratulaCreate, caratulaUpdate, caratulaDelete

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', inicio, name= 'index'),
     path('', ModalidadList.as_view(), name= 'index'),
    # path('agregar_modalidad/', agregarModalidad, name= 'agregar_modalidad'),
    path('agregar_modalidad/', ModalidadCreate.as_view(), name= 'agregar_modalidad'),
    # path('editar_modalidad/<int:id>/',editarModalidad, name = 'editar_modalidad'),
    path('editar_modalidad/<int:pk>/',ModalidadUpdate.as_view(), name = 'editar_modalidad'),
    # path('eliminar_modalidad/<int:id>/',eliminarModalidad, name = 'eliminar_modalidad'),
    path('eliminar_modalidad/<int:pk>/',ModalidadDelete.as_view(), name = 'eliminar_modalidad'),
    # ==============================================================================================
    path('', caratulaList.as_view(), name= 'index'),
    path('agregar_caratula/', caratulaCreate.as_view(), name= 'agregar_caratula'),
    path('editar_caratula/<int:pk>/',caratulaUpdate.as_view(), name = 'editar_caratula'),
    path('eliminar_caratula/<int:pk>/',caratulaDelete.as_view(), name = 'eliminar_caratula'),
]

# <int:pk> se debe utilizar cuando utilizamos vistas basadas en clases
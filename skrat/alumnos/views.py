from django.shortcuts import render, redirect
from django.template import Noticias, AreaNoticias
from django.contrib import messages
from django import loguot
from .form import NoticiasForm
#from django.http import HttpResponse
#def alumnos(request):
 #   return HttpResponse("Hello world!")
#def alumnos(request):
#  template = loader.get_template('Base.html')
#  return HttpResponse(template.render())
def Carrucel(request):
  return render(request,'alumnos/templates/Carrucel.html')
def Nosotros(request):
  return render(request,'alumnos/templates/Nosotros.html')
def Noticias(request):
  Noticias = Noticias.objects.all()
  context ={"Noticias":Noticias}
  return render(request,'alumnos/templates/Noticias.html', context)

#Gestion de Noticias
def gestionoti(request):
  Noticias = Noticias.objects.all()
  context = {"Noticias": Noticias}
  return render(request,'alumnos/templates/gestion/gestionoti.html', context)

#Crud -> Crear, Leer, Actualizar y Borrar
def nuevanoti(request):
  fromulario = NoticiasForm(request.post )


def salir(request):
    salir = loguot.
    return,
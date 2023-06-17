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
    formulario = NoticiasForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
       formulario.save()
       return redirect('gestionoti')
    return render(request, "alumnos/templates/gestion/nuevanoti.html", {"formulario": formulario})

def editarnoti(request, codigo):
    Noticias = Noticias.objects.get(codigo=codigo)
    formulario = NoticiasForm(request.POST or None, request.FILES or None, instance=Noticias)
    if formulario.is_valid() and request.POST:
       formulario.save()
       return redirect('gestionoti')
    return render(request, "alumnos/templates/gestion/editarnoti.html", {"formulario": formulario})

def eliminoti(request, codigo):
    Noticias = Noticias.objects.get(codigo=codigo)
    Noticias.delete()
    messages.success(request, '¡Noticia Eliminada!')
    return redirect('gestionoti')


def salir(request):
    salir = loguot
    return render(loguot)
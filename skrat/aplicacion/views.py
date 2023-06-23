from django.shortcuts import render, redirect
from .models import Noticias, AreaNoticias
from django.contrib import messages
#from django.contrib import logout
from .forms import NoticiasForm

#from django.http import HttpResponse
#def aplicacion1(request):
 #   return HttpResponse("Hello world!")
#def aplicacion2(request):
#  template = loader.get_template('Base.html')
#  return HttpResponse(template.render())

def home(request):
  return render(request,'home.html')

def Carrucel(request):
  return render(request,'Carrucel.html')

def Nosotros(request):
  return render(request,'Nosotros.html')

def Noticias(request):
  Noticia = Noticias.ob
  #context ={"Noticias":Noticia}
  context ={"Noticias":'Juan Pe'}
  return render(request,'Noticias.html',context)



#Gestion de Noticias
def gestionoti(request):
  Noticias = Noticias.objects.all()
  context = {"Noticias": Noticias}
  return render(request,'gestion/gestionoti.html', context)



#Crud -> Crear, Leer, Actualizar y Borrar
def nuevanoti(request):
    formulario = NoticiasForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
       formulario.save()
       return redirect('gestionoti')
    return render(request, "gestion/nuevanoti.html", {"formulario": formulario})

def editarnoti(request, codigo):
    Noticias = Noticias.objects.get(codigo=codigo)
    formulario = NoticiasForm(request.POST or None, request.FILES or None, instance=Noticias)
    if formulario.is_valid() and request.POST:
       formulario.save()
       return redirect('gestionoti')
    return render(request, "gestion/editarnoti.html", {"formulario": formulario})

def eliminoti(request, codigo):
    Noticias = Noticias.objects.get(codigo=codigo)
    Noticias.delete()
    messages.success(request, '¡Noticia Eliminada!')
    return redirect('gestionoti')


#def salir(request):
#    salir = logout
#    return render(logout)
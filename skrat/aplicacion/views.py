from django.shortcuts import render, redirect
from .models import Noticias, AreaNoticias
from django.contrib import messages
#from django.contrib import logout
from .forms import NoticiasForm

def home(request):
  return render(request,'home.html')
def Nosotros(request):
  return render(request,'Nosotros.html')
def Registrate(request):
  return render(request,'Registrate.html')
def Noticiass(request):
  noti = Noticias.objects.all()
  context = {"Noticiass": noti}
  return render(request,'Noticias.html', context)

#Gestion de Noticias
def gestionoti(request):
  noticias = Noticias.objects.all()
  context = {"Noticiass": noticias}
  return render(request,'gestion/gestionoti.html', context)

#Crud -> Crear, Leer, Actualizar y Borrar
def nuevanoti(request):
    formulario = NoticiasForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
       formulario.save()
       return redirect('gestionoti')
    return render(request, "gestion/nuevanoti.html", {"formulario": formulario})

def editarnoti(request, codigo):
    Noti = Noticias.objects.get(codigo=codigo)
    formulario = NoticiasForm(request.POST or None, request.FILES or None, instance=Noti)
    if formulario.is_valid() and request.POST:
       formulario.save()
       return redirect('gestionoti')
    return render(request, "gestion/editarnoti.html", {"formulario": formulario})

def eliminoti(request, codigo):
    Notic = Noticias.objects.get(codigo=codigo)
    Noticias.delete()
    messages.success(request, '¡Noticia Eliminada!')
    return redirect('gestionoti')


#def salir(request):
#    salir = logout
#    return render(logout)

#from django.http import HttpResponse
#def aplicacion1(request):
 #   return HttpResponse("Hello world!")
#def aplicacion2(request):
#  template = loader.get_template('Base.html')
#  return HttpResponse(template.render())
from django.shortcuts import render, redirect
from .models import Noticias, AreaNoticias, Usuarios
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .forms import NoticiasForm, UsuarioForm

def home(request):
  return render(request,'home.html')
def Contactanos(request):
   return render(request,'Contactanos.html')
def Nosotros(request):
  return render(request,'Nosotros.html')
def Registrate(request):
  return render(request,'Registrate.html')
def Noticiass(request):
  noti = Noticias.objects.all()
  context = {"Noticiass": noti}
  return render(request,'Noticias.html', context)
def Usuarioss(request):
   usua = Usuarios.objects.all()
   context = {"Usuarioss": usua}
   return render(request,'Nosotros.html', context)

#Gestion de Noticias
@login_required
def gestionoti(request):
  noticias = Noticias.objects.all()
  context = {"Noticiass": noticias}
  return render(request,'gestion/gestionoti.html', context)
#Crud -> Crear, Leer, Actualizar y Borrar
@login_required
def nuevanoti(request):
    formulario = NoticiasForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
       formulario.save()
       return redirect('gestionoti')
    return render(request, "gestion/nuevanoti.html", {"formulario": formulario})
@login_required
def editarnoti(request, codigo):
    Noti = Noticias.objects.get(codigo=codigo)
    formulario = NoticiasForm(request.POST or None, request.FILES or None, instance=Noti)
    if formulario.is_valid() and request.POST:
       formulario.save()
       return redirect('gestionoti')
    return render(request, "gestion/editarnoti.html", {"formulario": formulario})
@login_required
def eliminoti(request, codigo):
    Notic = Noticias.objects.get(codigo=codigo)
    Noticias.delete()
    messages.success(request, '¡Noticia Eliminada!')
    return redirect('gestionoti')

#Gestion de Usuarios
@login_required
def gestionuser(request):
  usua = Usuarios.objects.all()
  context = {"Usuarioss": usua}
  return render(request,'gestionuser/gestionuser.html',context)
#Crud -> Crear, Leer, Actualizar y Borrar
@login_required
def nuevouser(request):
    formulario = UsuarioForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
       formulario.save()
       return redirect('gestionuser')
    return render(request, "gestionuser/nuevouser.html", {"formulario": formulario})
@login_required
def editaruser(request, codigo):
    usua = Usuarios.objects.get(codigo=codigo)
    formulario = UsuarioForm(request.POST or None, request.FILES or None, instance=usua)
    if formulario.is_valid() and request.POST:
       formulario.save()
       return redirect('gestionuser')
    return render(request, "gestionuser/editaruser.html", {"formulario": formulario})
@login_required
def elimiuser(request, codigo):
    usua = Usuarios.objects.get(codigo=codigo)
    Usuarios.delete()
    messages.success(request, '¡Usuario Eliminada!')
    return redirect('gestionuser')


def login(request):
    return render(request, "login.html")

def salir(request):
    logout(request)
    return redirect('/')

#from django.http import HttpResponse
#def aplicacion1(request):
 #   return HttpResponse("Hello world!")
#def aplicacion2(request):
#  template = loader.get_template('Base.html')
#  return HttpResponse(template.render())
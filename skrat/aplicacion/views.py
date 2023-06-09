from django.shortcuts import render, get_object_or_404
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Noticias, UserProfile
from django.contrib import messages
from .forms import NoticiasForm

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

#C
@login_required
def nuevanoti(request):
    formulario = NoticiasForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
       formulario.save()
       return redirect('gestionoti')
    return render(request, "gestion/nuevanoti.html", {"formulario": formulario})
@login_required
def nuevousuario(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Usuario creado exitosamente.')
            return redirect('gestionusuario')
    else:
        form = UserCreationForm()
    context = {'form': form}
    return render(request, 'gestion/nuevousuario.html', context)

#R
@login_required
def gestionoti(request):
  Noti = Noticias.objects.all()
  context = {"Noticiass": Noti}
  return render(request,'gestion/gestionoti.html', context)
def gestionusuario(request):
    perfiles = UserProfile.objects.all()
    context = {'perfiles': perfiles}
    return render(request, 'gestion/gestionusuario.html', context)

#U
@login_required
def editarnoti(request, codigo):
    Noti = Noticias.objects.get(codigo=codigo)
    formulario = NoticiasForm(request.POST or None, request.FILES or None, instance=Noti)
    if formulario.is_valid() and request.POST:
       formulario.save()
       return redirect('gestionoti')
    return render(request, "gestion/editarnoti.html", {"formulario": formulario})
@login_required
def editarusuario(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if request.method == 'POST':
        form = UserChangeForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Usuario actualizado exitosamente.')
            return redirect('gestionusuario')
    else:
        form = UserChangeForm(instance=user)
    context = {'form': form, 'user': user}
    return render(request, 'gestion/editarusuario.html', context)

#D
@login_required
def eliminoti(request, codigo):
    Noti = Noticias.objects.get(codigo=codigo)
    Noticias.delete()
    messages.success(request, '¡Noticia Eliminada!')
    return redirect('gestionoti')
@login_required
def elimiusuario(request, codigo):
    usuarios = User.objects.all()
    usuarios.delete()
    messages.success(request, '¡Usuario Eliminado!')
    return redirect('gestionusuario')

#ENTRADA Y SALIDA
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Credenciales inválidas. Por favor, inténtalo nuevamente.')
    return render(request, "login.html")
@login_required
def logout(request):
    auth_logout(request)
    return redirect('home')
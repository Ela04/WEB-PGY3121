#Crear clases para formularios
from django import forms
from .models import Noticias, Usuarios
from django.forms import ModelForm

#Para ingresar noticias
class NoticiasForm(ModelForm):
    class Meta:
        model= Noticias
        #fields =['codigo','autor','nombre','fecha','contenido', 'img']
        
        fields = "__all__"

class UsuarioForm(ModelForm):
    class Meta:
        model= Usuarios
        #fields =['codigo', 'nombre','desc','img']
        
        fields = "__all__"
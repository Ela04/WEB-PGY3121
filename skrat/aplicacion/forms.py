#Para crear formularios
from django import forms
from .models import Noticias
from django.forms import ModelForm

#Para ingresar noticias
class NoticiasForm(ModelForm):
    class Meta:
        model= Noticias
        #fields =['codigo','autor','nombre','fecha','contenido', 'img']
        
        fields = "__all__"
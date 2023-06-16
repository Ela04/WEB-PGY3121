from socket import fromshare
from django import froms
from .models import alumnos

from django.forms import ModelForm
#Para ingresar noticias
class alumnosForm(ModelForm):
    class Meta:
        model= alumnos
        #fields =['id','autor','nombre','fecha','contenido']
        #
        fields = "__all__"
#Para ingresar al formulario
  
  
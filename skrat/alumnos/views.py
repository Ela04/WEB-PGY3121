

# Create your views here.
#from django.shortcuts import render
#from django.http import HttpResponse

#def alumnos(request):
 #   return HttpResponse("Hello world!")

from django.http import HttpResponse
from django.template import loader

def alumnos(request):
  template = loader.get_template('Base.html')
  return HttpResponse(template.render())


# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse

def alumnos(request):
    return HttpResponse("Hello world!")

from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    #path('alumnos/', views.alumnos, name='alumnos'),
    path('', views.home, name='home'),
    path('Base', views.Base, name='Base'),
    path('Carrucel', views.Carrucel, name='Carrucel'),
    path('Nosotros', views.Nosotros, name='Nosotros'),
    path('Noticias', views.Noticias, name='Noticias'),
    path('Registrate', views.Registrate, name='Registrate'),
]
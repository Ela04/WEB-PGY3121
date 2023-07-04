#from django.conf.urls import url
from django.urls import path, include
from  . import views
from django.conf.urls.static import static
from django.conf import settings 
from django.contrib import admin

urlpatterns = [
    path('', views.home, name='home'),
    path('menu', views.menu, name='menu'),
    path('Contactanos', views.Contactanos, name='Contactanos'),
    path('Nosotros', views.Nosotros, name='Nosotros'),
    path('Noticias', views.Noticiass, name='Noticias'),
    path('Registrate', views.Registrate, name='Registrate'),

    #C R U D
    path('gestionoti', views.gestionoti, name='gestionoti'),
    path('nuevanoti', views.nuevanoti, name='nuevanoti'),
    path('editarnoti/<codigo>', views.editarnoti, name='editarnoti'),
    path('eliminoti/<codigo>', views.eliminoti, name='eliminoti'),

    #path('login', views.login, name='login'),
    path('salir', views.salir, name='salir'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
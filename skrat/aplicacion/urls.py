#from django.conf.urls import url
from django.urls import path, include
from  . import views
from django.conf.urls.static import static
from django.conf import settings 
from django.contrib import admin
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    #path('menu', views.menu, name='menu'),
    path('Contactanos', views.Contactanos, name='Contactanos'),
    path('Nosotros', views.Nosotros, name='Nosotros'),
    path('Noticiass', views.Noticiass, name='Noticiass'),
    path('Registrate', views.Registrate, name='Registrate'),

    #C 
    path('nuevanoti/', views.nuevanoti, name='nuevanoti'),
    path('nuevousuario/', views.nuevousuario, name='nuevousuario'),
    #R
    path('gestionoti', views.gestionoti, name='gestionoti'),
    path('gestionusuario', views.gestionusuario, name='gestionusuario'),
    #U
    path('editarnoti/<codigo>/', views.editarnoti, name='editarnoti'),
    path('editarusuario/<int:user_id>/', views.editarusuario, name='editarusuario'),
    #D
    path('eliminoti/<codigo>/', views.eliminoti, name='eliminoti'),
    path('elimiusuario', views.elimiusuario, name='elimiusuario'),

    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
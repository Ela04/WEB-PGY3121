from django.urls import path
from . import views

urlpatterns = [
    path('alumna/', views.alumna, name='alumna'),
]
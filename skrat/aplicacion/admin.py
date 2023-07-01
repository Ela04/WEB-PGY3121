from django.contrib import admin
from .models import Usuarios, Noticias, AreaNoticias

# Register your models here.
admin.site.register(Noticias)
admin.site.register(AreaNoticias)
admin.site.register(Usuarios)

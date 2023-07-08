from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

class User(AbstractUser):
    img = models.ImageField(upload_to='profile_images/', blank=True, null=True)
    groups = models.ManyToManyField(Group, related_name='custom_user_set')
    user_permissions = models.ManyToManyField(Permission, related_name='custom_user_set')

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

class AreaNoticias(models.Model):
    idArea = models.AutoField(db_column='idArea', primary_key=True) 
    Descripcion = models.CharField(max_length=30, blank=False, null=False)

    def __str__(self):
        return str(self.Descripcion)

class Noticias(models.Model):
    codigo = models.CharField(primary_key=True, max_length=4, verbose_name='codigo')
    autor = models.CharField(max_length=50, verbose_name='autor')
    nombre = models.CharField(max_length=50, verbose_name='nombre')
    fecha = models.DateField(auto_now=False, verbose_name='fecha')
    Contenido = models.TextField(max_length=255, verbose_name='Contenido')
    idArea = models.ForeignKey('AreaNoticias', on_delete=models.CASCADE, db_column='idArea', verbose_name='idArea')
    img = models.ImageField(upload_to='media/img/', null=True, blank=True, verbose_name='img')

    def __str__(self):
        return str(self.nombre)

    class Meta:
        ordering = ['nombre']

    def delete(self, using=None, keep_parents=False):
        self.img.storage.delete(self.img.name)
        return super().delete()
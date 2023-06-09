from django.db import models

# Create your models here.
class alumnos(models.Model):
  Nombre = models.CharField(max_length=255)
  Correo = models.CharField(max_length=255)
  Contraseña = models.CharField(max_length=8)


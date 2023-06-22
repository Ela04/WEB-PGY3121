from django.db import models

# Create your models here.
class AreaNoticias(models.Model):
  idArea = models.AutoField(db_column='idArea', primary_key=True) 
  Descripcion = models.CharField(max_length=30, blank=False, null=False)

  def __str__(self):
    return str(self.Descripcion)

class Noticias(models.Model):
  codigo = models.CharField(primary_key=True, ma_length=4, verbose_name='codigo')
  autor = models.CharField(max_length=50, verbose_name='autor')
  nombre = models.CharField(max_length=50, verbose_name='nombre')
  fecha = models.DateField(auto_now=False, verbose_name='fecha')
  Contenido = models.CharField(max_length=255, verbose_name='Contenido')
  idArea = models.ForeignKey('AreaNoticias',on_delete=models.CASCADE, db_colum='idArea', verbose_name='idArea')
  img =models.ImageField(upload_to='img/', null=True, blank=True,verbose_name='img')
  
  #Funcion para ordenar por la fecha
  def __str__(self):
    return str(self.fecha)
  class Meta:
    ordening =['fecha']

  #Funcion para eliminar
  def delete(self, using=None, keep_parents=False):
    self.img.storage.delete(self.img.name)
    return super().delete()
from distutils.command.upload import upload
# from tabnanny import verbose
from django.db import models

# Create your models here.

# class Categoria(models.Model):
#     titulo = models.CharField(max_length=50)
#     imagen = models.ImageField(upload_to='categorias')

#     class Meta:
#         verbose_name = 'categoria'
#         verbose_name_plural = 'categorias'
        
#     def __str__(self):
        
#         return self.titulo
    
    
class Productos(models.Model):
    producto = models.CharField(max_length=50)
    marca = models.CharField(max_length=50)
    seccion = models.CharField(max_length=50)
    cantidad = models.IntegerField()
    precio = models.IntegerField()
    
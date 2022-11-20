from django.db import models


# Create your models here.


class user(models.Model):
    username = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=25)
    imagen = models.ImageField(upload_to='Users')
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    
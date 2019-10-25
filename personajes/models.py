from django.db import models

class Personaje(models.Model):
    nombre = models.CharField(max_length=128)
    nombre_real = models.CharField(max_length=128)
    imagen = models.ImageField()
    descripcion = models.TextField()
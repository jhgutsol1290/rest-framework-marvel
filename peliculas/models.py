from django.db import models

class Pelicula(models.Model):
    nombre = models.CharField(max_length=128)
    director = models.CharField(max_length=128)
    sinopsis = models.TextField()
from rest_framework import serializers
from peliculas.models import Pelicula

class PeliculaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pelicula
        fields = ('id', 'nombre', 'director', 'sinopsis')
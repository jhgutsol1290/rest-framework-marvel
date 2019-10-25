from rest_framework import serializers
from personajes.models import Personaje

class PersonajeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Personaje
        fields = ('id', 'nombre', 'nombre_real', 'imagen', 'descripcion')
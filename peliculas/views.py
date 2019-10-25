from django.shortcuts import render
from rest_framework import viewsets
from .models import Pelicula
from .serializers import PeliculaSerializer

class PeliculasViewSet(viewsets.ModelViewSet):
    queryset = Pelicula.objects.all().filter()

    serializer_class = PeliculaSerializer

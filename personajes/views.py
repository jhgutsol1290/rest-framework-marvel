from django.shortcuts import render
from rest_framework import viewsets
from .models import Personaje
from .serializers import PersonajeSerializer

class PersonajesViewSet(viewsets.ModelViewSet):
    queryset = Personaje.objects.all().filter()

    serializer_class = PersonajeSerializer
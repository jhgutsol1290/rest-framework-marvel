from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from personajes.views import PersonajesViewSet
from peliculas.views import PeliculasViewSet

router = routers.DefaultRouter()
router.register('personajes', PersonajesViewSet)
router.register('peliculas', PeliculasViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]

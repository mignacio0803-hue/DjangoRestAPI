from rest_framework import viewsets
from estudiantes.models import Estudiantes
from estudiantes.api.serializer import EstudiantesSerializer

class EstudiantesViewSet(viewsets.ModelViewSet):
    queryset = Estudiantes.objects.all()
    serializer_class = EstudiantesSerializer
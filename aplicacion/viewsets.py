#viewsets.py
from rest_framework import viewsets
from .models import Sensor, Medicion
from .serializers import SensorSerializer, MedicionSerializer

class SensorViewSet(viewsets.ModelViewSet):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

class MedicionViewSet(viewsets.ModelViewSet):
    queryset = Medicion.objects.all()
    serializer_class = MedicionSerializer
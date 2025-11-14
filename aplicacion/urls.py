#urls.py
from django.urls import path, include
from rest_framework import routers
from .viewsets import SensorViewSet, MedicionViewSet

router = routers.DefaultRouter()
router.register(r'sensores', SensorViewSet)
router.register(r'mediciones', MedicionViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
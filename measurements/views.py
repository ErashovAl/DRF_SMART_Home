from rest_framework.viewsets import ModelViewSet

from .serializers import SensorSerializer, MeasurementSerializer
from .models import Sensor, Measurement


class SensorViewSet(ModelViewSet):
    """ViewSet для проекта."""
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer



class MeasurementViewSet(ModelViewSet):
    """ViewSet для измерения."""
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer
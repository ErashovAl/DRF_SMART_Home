from django.urls import include
from django.urls import path

from rest_framework.routers import DefaultRouter
from measurements.views import SensorViewSet, MeasurementViewSet

router = DefaultRouter()
router.register('measurements', MeasurementViewSet)
router.register('sensors', SensorViewSet)

urlpatterns = [
    
    path('api/', include(router.urls)),

]
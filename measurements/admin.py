from django.contrib import admin

from .models import Sensor, Measurement

@admin.register(Sensor)
class SensorAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'created_at']

@admin.register(Measurement)
class MesurmentAdmin(admin.ModelAdmin):
    list_display = ['id', 'temperature', 'sensor', 'created_at']
from django.db import models

class TimeStampFields(models.Model):

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Sensor(TimeStampFields):
    """Объект на котором проводят измерения."""

    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)

    def __str__(self) -> str:
        return self.name

class Measurement(TimeStampFields):
    """Измерение температуры на объекте."""

    temperature = models.FloatField()
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='measurements')
    
    attachments = models.ImageField(
        upload_to='static/images/',
        height_field=None,
        width_field=None,
        max_length=12000,
        null=True
    ) 

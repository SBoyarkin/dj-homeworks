from django.db import models


class Sensor(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='Название датчика')
    description = models.CharField(max_length=250, default='undefined', verbose_name='Расположение')

    def __str__(self):
        return self.name


class Measurement(models.Model):
    sensor_id = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='measurement')
    temperature = models.FloatField(verbose_name='Температура')
    created_at = models.DateTimeField(auto_now=True, verbose_name='Дата и время измерения')


# TODO: опишите модели датчика (Sensor) и измерения (Measurement)

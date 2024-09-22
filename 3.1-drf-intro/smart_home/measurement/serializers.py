from rest_framework import serializers
from .models import Sensor, Measurement




class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description']



class MeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = ['id', 'temperature','created_at',]


class InfoSerializer(serializers.ModelSerializer):
    measurement = MeasurementSerializer(read_only=True, many=True,)
    class Meta:
        model = Sensor

        fields = ['id', 'name', 'description', 'measurement']

# TODO: опишите необходимые сериализаторы

# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.generics import ListCreateAPIView, ListAPIView, RetrieveUpdateAPIView
from rest_framework.response import Response
from .models import Sensor, Measurement
from .serializers import SensorSerializer, MeasurementSerializer, InfoSerializer
from rest_framework.exceptions import NotFound


class SensorListAPIView(ListAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

    def post(self, request):
        name = request.POST.get('name')
        description = request.POST.get('description')
        if name:
            obj = Sensor()
            obj.name = name
            obj.description = description
            obj.save()
            return Response('status: 201')
        else:
            return Response('status: 400')


class MeasurementListAPIView(ListAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer
    def post(self, request):
        sensor_id = request.POST.get('sensor_id')
        temperature = request.POST.get('temperature')
        if sensor_id and temperature:
            obj = Measurement()
            obj.sensor_id = Sensor(sensor_id)
            obj.temperature = temperature
            obj.save()
            return Response('status: 201')
        else:
            return Response('status: 400')

class InfoListAPIView(ListAPIView):
    queryset = Sensor.objects.all()
    serializer_class = InfoSerializer



class UpdateSensorRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

    def get(self, request, pk):
        print(request, pk)
        obj = Sensor.objects.get(id=pk)
        serializer = self.serializer_class(obj)
        print(serializer)
        if obj:
            return Response(serializer.data)
        else:
            raise NotFound
from django.urls import path

from measurement.views import SensorListAPIView, MeasurementListAPIView, InfoListAPIView, \
    UpdateSensorRetrieveUpdateAPIView

urlpatterns = [
    path('sensor/', SensorListAPIView.as_view()),
    path('update-sensor/<pk>', UpdateSensorRetrieveUpdateAPIView.as_view()),
    path('measurement/', MeasurementListAPIView.as_view()),
    path('info/', InfoListAPIView.as_view()),
    # TODO: зарегистрируйте необходимые маршруты
]

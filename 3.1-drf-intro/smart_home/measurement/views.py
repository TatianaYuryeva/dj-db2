# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView

from measurement.models import Sensor, Measurement
from measurement.serializers import SensorSerializer, SensorDetailSerializer, CreateMeasurementSerializer


class ListCreateSensors(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class RetrieveUpdateSensor(RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer


class CreateMeasurement(CreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = CreateMeasurementSerializer


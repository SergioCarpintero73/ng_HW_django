from rest_framework.response import Response
from rest_framework.generics import UpdateAPIView, RetrieveAPIView, ListAPIView, CreateAPIView
from .models import Sensor, Measurement
from .serializers import SensorsSerializer, MeasurementsSerializer


class SensorListView(ListAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorsSerializer

    def post(self, request):
        Sensor.objects.create(title=request.data['title'], description=request.data['description'])
        return Response({'status': 'OK'})


class SensorRetrieveView(RetrieveAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorsSerializer


class SensorUpdateView(UpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorsSerializer


class MeasurementCreateView(CreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementsSerializer
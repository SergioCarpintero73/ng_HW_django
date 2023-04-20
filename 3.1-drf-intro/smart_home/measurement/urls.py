from django.urls import path
from .views import SensorUpdateView, SensorRetrieveView, SensorListView, MeasurementCreateView

urlpatterns = [
    path('sensors/', SensorListView.as_view()),
    path('sensor/up/<pk>/', SensorUpdateView.as_view()),
    path('sensor/<pk>/', SensorRetrieveView.as_view()),
    path('measurements/', MeasurementCreateView.as_view()),
]
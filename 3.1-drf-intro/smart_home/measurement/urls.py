from django.urls import path

from .views import SensorsView, MeasurementView, SensorViewUpdate

urlpatterns = [
    path('sensors/', SensorsView.as_view()),
    path('sensors/<pk>/', SensorViewUpdate.as_view()),
    path('measurements/', MeasurementView.as_view()),
]
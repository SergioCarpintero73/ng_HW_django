from django.db import models


class Sensor(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=300, blank=True)


class Measurement(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE)
    temperature = models.IntegerField()
    date_meas = models.DateField(auto_now_add=True)
    time_meas = models.TimeField(auto_now_add=True)
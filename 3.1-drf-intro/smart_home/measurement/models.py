from django.db import models


class Sensor(models.Model):
    name = models.CharField(max_length=50, verbose_name='Имя датчика')
    description = models.TextField(max_length=80, verbose_name='Описание')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['id']


class Measurement(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, verbose_name='Датчик', related_name='measurements')
    temperature = models.FloatField(verbose_name='Температура')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

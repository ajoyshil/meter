import datetime

from django.db import models

# Create your models here.


class Meter(models.Model):
    label = models.CharField(max_length=255, null=False, blank=False)


class MeterData(models.Model):
    meter_id = models.ForeignKey(Meter, null=False, blank=False, on_delete=models.CASCADE)
    value = models.IntegerField(default=0)
    timestamp = models.DateTimeField(auto_now_add=datetime.datetime.now())

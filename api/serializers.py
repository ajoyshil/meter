from .models import Meter, MeterData
from rest_framework import serializers
from .views import *


class MeterSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="meter-detail")
    class Meta:
        model = Meter
        fields = ["url", 'label']


class MeterDataSerializer(serializers.ModelSerializer):
    # value = serializers.IntegerField()
    class Meta:
        model = MeterData
        fields = ["id", "value", "timestamp"]

        # def create(self, validate_data):
        #     meter_id = validate_data.pop("meter_id")
        #     meter = Meter.objects.get(pk=meter_id)
        #     meter_data = MeterData(
        #         meter_id = meter,
        #         value = validate_data.pop("value")
        #     )
        #     return meter_data.save()

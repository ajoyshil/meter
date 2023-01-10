from django.shortcuts import render
from .serializers import MeterSerializer, MeterDataSerializer
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from .models import Meter, MeterData


# class MeterViewSet(ModelViewSet):
#     queryset = Meter.objects.all()
#     serializer_class = MeterSerializer
#     permission_classes = ()
#     http_method_names = ['get', 'post']


class MeterView(APIView):

    def get(self, request):
        meter = Meter.objects.all()
        serializer = MeterSerializer(meter, many=True, context={'request': request})
        print(serializer.data)
        return Response(serializer.data)
    #
    # def post(self, request, format=None):
    #     serializer = MeterSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MeterDetailView(APIView):

    def get(self, request, pk, format=None):
        meter = Meter.objects.get(pk=pk)
        meterdata = MeterData.objects.filter(meter_id=meter)
        serializer = MeterDataSerializer(meterdata, many=True)
        return Response(serializer.data)


class MeterDataView(APIView):

    def get(self, request, pk, format=None):
        meter = Meter.objects.get(pk=pk)
        meterdata = MeterData.objects.filter(meter_id=meter)
        serializer = MeterDataSerializer(meterdata, many=True)
        return Response(serializer.data)

    def post(self, request,pk, format=None):
        serializer = MeterDataSerializer(data=request.data)
        if serializer.is_valid():
            # meter = Meter.objects.get(pk=request.data.)
            meter = Meter.objects.get(pk=pk)
            serializer.save(meter_id=meter)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)






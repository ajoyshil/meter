from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('meters/', MeterView.as_view()),
    path('meters/<int:pk>', MeterDetailView.as_view(), name='meter-detail'),
    # path('meters_data/', MeterDataView.as_view()),
    path('meters_data/<int:pk>', MeterDataView.as_view()),
]

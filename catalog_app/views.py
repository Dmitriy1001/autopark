from rest_framework import generics

from .serializers import DriverSerializer
from .models import Driver, Vehicle


class DriverList(generics.ListAPIView):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer


class DriverDetail(generics.RetrieveAPIView):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer
    lookup_url_kwarg = 'driver_id'


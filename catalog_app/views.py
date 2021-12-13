from rest_framework import generics

from .serializers import DriverSerializer
from .models import Driver, Vehicle


class DriverList(generics.ListCreateAPIView):
    serializer_class = DriverSerializer

    def get_queryset(self):
        params = self.request.GET
        if 'created_at__gte' in params:
            valid_date = '-'.join(params['created_at__gte'].split('-')[::-1])
            return Driver.objects.filter(created_at__gte=valid_date)
        elif 'created_at__lte' in params:
            valid_date = '-'.join(params['created_at__lte'].split('-')[::-1])
            return Driver.objects.filter(created_at__lte=valid_date)
        return Driver.objects.all()


class DriverDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer
    lookup_url_kwarg = 'driver_id'


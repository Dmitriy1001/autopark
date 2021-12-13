from rest_framework import generics

from .models import Driver, Vehicle
from .serializers import DriverSerializer, VehicleSerializer, VehicleSetDriverSerializer


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


class VehicleList(generics.ListCreateAPIView):
    serializer_class = VehicleSerializer

    def get_queryset(self):
        params = self.request.GET
        if 'with_drivers' in params:
            is_null = False if params['with_drivers'].lower() == 'yes' else True
            return Vehicle.objects.filter(driver_id__isnull=is_null).select_related('driver_id')
        return Vehicle.objects.select_related('driver_id')


class VehicleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vehicle.objects.select_related('driver_id')
    serializer_class = VehicleSerializer
    lookup_url_kwarg = 'vehicle_id'


class VehicleSetDriver(generics.RetrieveUpdateAPIView):
    queryset = Vehicle.objects.select_related('driver_id')
    serializer_class = VehicleSetDriverSerializer
    lookup_url_kwarg = 'vehicle_id'

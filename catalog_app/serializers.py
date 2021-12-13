from rest_framework import serializers

from .models import Driver, Vehicle


class DriverSerializer(serializers.ModelSerializer):
    cars = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Driver
        fields = ('id', 'first_name', 'last_name', 'created_at', 'updated_at', 'cars')


class VehicleSerializer(serializers.ModelSerializer):
    driver_id = serializers.ReadOnlyField(source='driver_id.id')

    class Meta:
        model = Vehicle
        fields = (
            'id',
            'driver_id',
            'make',
            'model',
            'plate_number',
            'created_at',
            'created_at',
            'updated_at',
        )


class VehicleSetDriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = ('driver_id',)

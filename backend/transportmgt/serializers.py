from rest_framework import serializers
from . models import Bus, BusCompany, Driver, Bookings, Route

class BusSerializer(serializers.Serializer):
    class Meta:
        model = Bus
        fields = '__all__'

class BusCompanySerializer(serializers.Serializer):
    class Meta:
        model = BusCompany
        fields = '__all__'

class DriverSerializer(serializers.Serializer):
    class Meta:
        model = Driver
        fields = '__all__'

class BookingsSerializer(serializers.Serializer):
    class Meta:
        model = Bookings
        fields = '__all__'

class RouteSerializer(serializers.Serializer):
    class Meta:
        model = Route
        fields = '__all__'


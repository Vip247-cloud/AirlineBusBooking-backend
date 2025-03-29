from rest_framework import serializers
from .models import Flight, Passenger, Booking


class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = '__all__'


class PassengerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passenger
        fields = '__all__'


# class BookingSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Booking
#         fields = '__all__'

class BookingSerializer(serializers.ModelSerializer):
    flight_number = serializers.CharField(source='flight.flight_number', read_only=True)
    passenger_name = serializers.SerializerMethodField()

    class Meta:
        model = Booking
        fields = ['id', 'seat_number', 'booking_date', 'status', 'flight', 'flight_number', 'passenger', 'passenger_name']

    def get_passenger_name(self, obj):
        return f"{obj.passenger.first_name} {obj.passenger.last_name}"


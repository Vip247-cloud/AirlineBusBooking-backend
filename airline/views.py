from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Flight, Passenger, Booking
from .serializers import FlightSerializer, PassengerSerializer, BookingSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from .public_api import get_flights


from rest_framework import status
from rest_framework.decorators import api_view
from .models import Flight
from .serializers import FlightSerializer


class FlightViewSet(viewsets.ModelViewSet):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer


class PassengerViewSet(viewsets.ModelViewSet):
    queryset = Passenger.objects.all()
    serializer_class = PassengerSerializer


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer




class PublicFlightSearchView(APIView):
    def get(self, request):
        origin = request.query_params.get("origin")
        destination = request.query_params.get("destination")

        if not origin or not destination:
            return Response({"error": "Please provide origin and destination."}, status=400)

        data = get_flights(origin, destination)
        return Response(data)


@api_view(['POST'])
def import_public_flight(request):
    data = request.data  # JSON payload from frontend/public API
    try:
        flight = Flight.objects.create(
            flight_number=data['flight_number'],
            origin=data['origin'],
            destination=data['destination'],
            departure_time=data['departure_time'],
            arrival_time=data['arrival_time'],
            airline=data['airline'],
            price=data['price']
        )
        return Response(FlightSerializer(flight).data, status=201)
    except Exception as e:
        return Response({'error': str(e)}, status=400)


from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Flight
from .serializers import FlightSerializer
import requests

class CombinedTravelOptionsView(APIView):
    def get(self, request):
        origin = request.query_params.get('from')
        destination = request.query_params.get('to')

        if not origin or not destination:
            return Response({'error': 'Please provide origin and destination'}, status=400)

        # Flights from your DB
        flights = Flight.objects.filter(origin__iexact=origin, destination__iexact=destination)
        flight_data = FlightSerializer(flights, many=True).data

        # Buses from classmate's API
        try:
            bus_api_url = f"http://127.0.0.1:8002/api/routes/?from={origin}&to={destination}"
            bus_response = requests.get(bus_api_url)
            bus_data = bus_response.json()
        except Exception as e:
            bus_data = {'error': str(e)}

        return Response({
            'origin': origin,
            'destination': destination,
            'flights': flight_data,
            'buses': bus_data
        })

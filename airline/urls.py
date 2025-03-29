from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FlightViewSet, PassengerViewSet, BookingViewSet, PublicFlightSearchView


from .views import import_public_flight

from .views import (
    FlightViewSet,
    PassengerViewSet,
    BookingViewSet,
    PublicFlightSearchView,
    CombinedTravelOptionsView,  # 🔥 <--- This was missing
)


router = DefaultRouter()
router.register('flights', FlightViewSet)
router.register('passengers', PassengerViewSet)
router.register('bookings', BookingViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('search/', PublicFlightSearchView.as_view(), name='public-flight-search'),
    path('import/', import_public_flight, name='import-public-flight'),
    path('search-combined/', CombinedTravelOptionsView.as_view(), name='combined-search'),


]

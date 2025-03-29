from django.urls import path
from .views import BusRouteView

urlpatterns = [
    path('routes/', BusRouteView.as_view(), name='bus-routes'),
]

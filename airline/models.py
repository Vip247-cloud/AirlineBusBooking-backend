from django.db import models

class Flight(models.Model):
    flight_number = models.CharField(max_length=10)
    origin = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()
    airline = models.CharField(max_length=100)
    # price = models.DecimalField(max_digits=8, decimal_places=2)
    price = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.flight_number} - {self.origin} → {self.destination}"


class Passenger(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Booking(models.Model):
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    passenger = models.ForeignKey(Passenger, on_delete=models.CASCADE)
    seat_number = models.CharField(max_length=10)
    booking_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=[("confirmed", "Confirmed"), ("cancelled", "Cancelled")], default="confirmed")

    def __str__(self):
        return f"Booking #{self.id} - {self.passenger} on {self.flight}"

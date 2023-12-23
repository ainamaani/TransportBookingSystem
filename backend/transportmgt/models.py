from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class BusCompany(models.Model):
    name = models.CharField(max_length=30)
    number_of_buses = models.PositiveIntegerField()
    location_district = models.CharField(max_length=20)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)

    def __str__(self) -> str:
        return self.name
    
class Bus(models.Model):

    class BusChoices(models.TextChoices):
        ORDINARY = "OD",("Ordinary")
        EXECUTIVE = "EX",("Executive")

    name = models.CharField(max_length=20)
    number_plate = models.CharField(max_length=20)
    seats = models.IntegerField(default=67)
    company = models.ForeignKey(BusCompany, on_delete=models.CASCADE, related_name='companies')
    type = models.CharField(max_length=20, default="OD", choices=BusChoices.choices)

    def __str__(self) -> str:
        return self.name

class Route(models.Model):
    name = models.CharField(max_length=20)
    bus = models.ForeignKey(Bus, on_delete=models.CASCADE, related_name='buses')
    company = models.ForeignKey(BusCompany, on_delete=models.CASCADE, related_name='companies')
    start_location = models.CharField(max_length=20)
    end_location = models.CharField(max_length=20)
    fare = models.DecimalField(max_digits=8, decimal_places=2)
    time = models.TimeField()
    date = models.DateField()

    def __str__(self) -> str:
        return self.name

class Bookings(models.Model):
    class BookingsChoices(models.TextChoices):
        PAID = "PD",("Paid")
        PENDING = "PN",("Pending")

    route = models.ForeignKey(Route, on_delete=models.DO_NOTHING, related_name='routes')
    company = models.ForeignKey(BusCompany, on_delete=models.CASCADE, related_name='companies')
    bus = models.ForeignKey(Bus, on_delete=models.CASCADE, related_name='buses')
    date = models.DateField()
    customer = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='customers')
    seat_number = models.IntegerField()
    payment_status = models.CharField(max_length=20, default="PN", choices=BookingsChoices.choices)

    def __str__(self) -> str:
        return self.route
    
class Driver(models.Model):
    name = models.CharField(max_length=20)
    company = models.ForeignKey(BusCompany, on_delete=models.CASCADE, related_name='companies')
    route = models.ForeignKey(Route, on_delete=models.DO_NOTHING, related_name='routes')
    bus = models.ForeignKey(Bus, on_delete=models.CASCADE, related_name='buses')
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.name



    

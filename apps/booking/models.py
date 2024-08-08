from django.db import models
from django.utils.timezone import now
from django.core.validators import MinValueValidator

from apps.general.models import General
from apps.stations.models import StationPetrolMark


class Bookings(models.Model):
    station = models.ForeignKey('stations.Station', on_delete=models.PROTECT, related_name='bookings')
    
    car = models.ForeignKey('cars.UserCar', on_delete=models.SET_NULL, null=True, related_name='bookings')
    car_number = models.CharField(max_length=100)
    car_model = models.CharField(max_length=100)

    petrol_mark = models.PositiveSmallIntegerField(choices=StationPetrolMark.PetrolMarks.choices)
    quantity = models.PositiveSmallIntegerField()
    booking_time = models.DateTimeField(validators=[MinValueValidator(now)])
    minutes = models.PositiveSmallIntegerField()

    def save(self, *args, **kwargs):
        if not self.car_number:
            self.car_number = self.car.number
        if not self.car_model:
            self.car_model = self.car.model

        if not self.pk:
            user = self.car.user
            user.balance = max(user.balance - getattr(General.objects.first(), 'booking_price', 0), 0)
        super().save(*args, **kwargs)        

    def __str__(self):
        return f'{self.car} - {self.station} - {self.datetime}'
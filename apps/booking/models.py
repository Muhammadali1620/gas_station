from django.db import models
from django.utils.timezone import now
from django.core.validators import MinValueValidator
from django.conf import settings

from apps.general.models import General
from apps.stations.models import StationPetrolMark


class Booking(models.Model):
    station = models.ForeignKey('stations.Station', on_delete=models.SET_NULL, null=True, related_name='bookings')
    station_petrol_mark = models.ForeignKey('stations.StationPetrolMark', on_delete=models.SET_NULL, null=True)
    petrol_mark = models.PositiveSmallIntegerField(choices=StationPetrolMark.PetrolMarks.choices)

    car = models.ForeignKey('cars.UserCar', on_delete=models.SET_NULL, null=True, related_name='bookings')
    car_number = models.CharField(max_length=100)
    car_model = models.CharField(max_length=100)

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)

    quantity = models.PositiveSmallIntegerField(validators=[MinValueValidator(1)])
    booking_time = models.DateTimeField(validators=[MinValueValidator(now)])
    minutes = models.PositiveSmallIntegerField(editable=False)

    def save(self, *args, **kwargs):
        if not self.car_number:
            self.car_number = self.car.number
        if not self.car_model:
            self.car_model = self.car.model

        if not self.station_id:
            self.station_id = self.station_petrol_mark.station_id
        if not self.petrol_mark:
            self.petrol_mark = self.station_petrol_mark.petrol_mark

        if not self.minutes:
            self.minutes = round(self.station_petrol_mark.fueling_time * self.quantity / 60, 0
                                 ) + General.get_booking_extra_time()

        if not self.pk:
            user = self.car.user
            user.balance = max(user.balance - General.get_booking_price(), 0)
            user.save()
        super().save(*args, **kwargs)        

    def __str__(self):
        return f'{self.car} - {self.station} - {self.booking_time}'
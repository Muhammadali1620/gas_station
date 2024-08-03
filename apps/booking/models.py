from django.db import models

from apps.stations.models import StationPetrolMark


class Bookings(models.Model):
    car = models.ForeignKey('cars.UserCar', on_delete=models.CASCADE, related_name='bookings')
    station = models.ForeignKey('stations.Station', on_delete=models.CASCADE, related_name='bookings')
    petrol_mark = models.PositiveSmallIntegerField(choices=StationPetrolMark.PetrolMarks.choices)
    quantity = models.PositiveSmallIntegerField()
    datetime = models.DateTimeField()
    minutes = models.PositiveSmallIntegerField(blank=True, null=True)

    def __str__(self):
        return f'{self.car} - {self.station} - {self.datetime}'
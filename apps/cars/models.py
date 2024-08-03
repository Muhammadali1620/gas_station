from django.db import models

from apps.cars.validators import validate_car_number
from django.contrib.postgres.fields import ArrayField

from apps.stations.models import StationPetrolMark


class UserCar(models.Model):
    class CarModel(models.IntegerChoices):
        OTHER = 0, 'ДРУГАЯ'
        NEXIA_1 = 1, 'NEXIA 1'
        NEXIA_2 = 2, 'NEXIA 2'
        NEXIA_3 = 4,'NEXIA 3'
        MALIBU = 5, 'MALIBU'
        GENTRA = 6, 'GENTRA'
        TRAKER = 7, 'TRAKER'
        MATIZ = 8, 'MATIZ'
        SPARK = 9, 'SPARK'
        EPICA = 10, 'EPICA'
        LACETTI = 11, 'LACETTI'
        TICO = 12, 'TICO'
        CAPTIVA = 13, 'CAPTIVA'
        COBALT = 14, 'COBALT'
    
    class CarColor(models.IntegerChoices):
        OTHER = 0, 'ДРУГИЕ'
        BLACK = 1, 'ЧОРНЫЙ'
        WHITE = 2, 'БЕЛЫЙ'
        GREY = 3, 'СЕРЫЙ'

    class CarCategory(models.IntegerChoices):
        SEDAN = 1, 'Седан'
        COUPE = 2, 'Купе'
        HATCHBACK = 3, 'Хэтчбек'
        LIFTBACK = 4, 'Лифтбек'
        FASTBACK = 5, 'Фастбэк'
        STATION_WAGON = 6, 'Универсал'
        CROSSOVER = 7, 'Кроссовер'
        SUV = 8, 'Внедорожник'

    user = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE)
    number = models.CharField(max_length=10, validators=[validate_car_number], unique=True)
    model = models.PositiveSmallIntegerField(choices=CarModel.choices, default=CarModel.OTHER)
    color = models.PositiveSmallIntegerField(choices=CarColor.choices, default=CarColor.OTHER, blank=True, null=True)
    category = models.PositiveSmallIntegerField(choices=CarCategory.choices)
    petrol_mark = ArrayField(base_field=models.PositiveSmallIntegerField(choices=StationPetrolMark.PetrolMarks.choices, blank=True, null=True))

    def __str__(self):
        return self.number
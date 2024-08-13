from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.core.exceptions import ValidationError

from colorfield.fields import ColorField

from apps.cars.validators import validate_car_number
from apps.stations.models import StationPetrolMark


class CarModel(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    parent = models.ForeignKey('self', on_delete=models.PROTECT,  blank=True, null=True)

    def clean(self):
        if not self.pk and self.parent:
            if self.parent.parent:
                if self.parent.parent.parent:
                    raise ValidationError({'parent': 'Модель автомобиля не может быть родительской моделью'})
        
    def __str__(self):
        return self.name


class UserCar(models.Model):
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
    number = models.CharField(max_length=10, db_index=True, validators=[validate_car_number], unique=True)
    model = models.ForeignKey(CarModel, on_delete=models.PROTECT)
    color = ColorField(default='#FF0000')
    petrol_mark = ArrayField(base_field=models.PositiveSmallIntegerField(choices=StationPetrolMark.PetrolMarks.choices),blank=True, null=True)

    def __str__(self):
        return self.number
    

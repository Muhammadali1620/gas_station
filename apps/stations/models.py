from django.db import models
from django.core.validators import MinValueValidator
from django.contrib.postgres.fields import ArrayField


class Station(models.Model):
    class Comforts(models.IntegerChoices):
        WIFI = 1, 'WIFI'
        SHOP = 2, 'SHOP'
        GAME_CLUB = 3, 'GAME_CLUB'
        FOOD = 4, 'FOOD'

    name = models.CharField(max_length=100)
    short_text = models.CharField(max_length=255)
    logo = models.ImageField(upload_to='stations/logos')
    rating = models.FloatField(default=0.0, blank=True)
    address = models.CharField(max_length=150)
    latitude = models.PositiveIntegerField()
    longitude = models.PositiveIntegerField()
    video = models.FileField(upload_to='stations/videos', blank=True)
    comforts = ArrayField(base_field=models.PositiveSmallIntegerField(choices=Comforts.choices, blank=True, null=True))

    def __str__(self):
        return self.name


class StationImage(models.Model):
    station = models.ForeignKey(Station, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='stations/images')
    order = models.PositiveSmallIntegerField(default=1, validators=[MinValueValidator(1)])

    class Meta():
        unique_together = ('station', 'order')


class StationWorkTime(models.Model):
    class WeekDays(models.IntegerChoices):
        MONDAY = 1, 'Понедельник'
        TUESDAY = 2, 'Вторник'
        WEDNESDAY = 3, 'Среда'
        THURSDAY = 4, 'Четверг'
        FRIDAY = 5, 'Пятница'
        SATURDAY = 6, 'Суббота'
        SUNDAY = 7, 'Воскресенье'

    week_days = models.PositiveSmallIntegerField(choices=WeekDays.choices, default=1)
    station = models.ForeignKey(Station, on_delete=models.CASCADE, related_name='work_times')
    week_day = models.PositiveSmallIntegerField(choices=WeekDays.choices)
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return f'{self.get_week_day_display()}: {self.start_time} - {self.end_time}'


class StationPetrolMark(models.Model):
    class PetrolMarks(models.IntegerChoices):
        A_80 = 1, 'A-80'
        A_90 = 2, 'A-90'
        A_91 = 3, 'A-91'
        A_92 = 4, 'A-92'
        A_95 = 5, 'A-95'
        A_98 = 6, 'A-98'
        A_100 = 7, 'A-100'
        A_101 = 8, 'A-101'    
        DIESEL = 9, 'DIESEL'
        METAN = 10, 'METAN'
        PROPAN = 11, 'PROPAN'
        ELECTR = 12, 'ELECTR'

    station = models.ForeignKey(Station, on_delete=models.CASCADE, related_name='petrol_marks')
    petrol_mark = models.PositiveSmallIntegerField(choices=PetrolMarks.choices)
    number_of_columns = models.PositiveSmallIntegerField(default=1, validators=[MinValueValidator(1)])
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0, validators=[MinValueValidator(0)])
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.get_petrol_mark_display()}: {self.price}'
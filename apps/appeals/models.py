from django.db import models

from apps.users.validators import phone_validate


class Appeal(models.Model):
    class Section(models.IntegerChoices):
        STATION_CREATION = 0, 'Создание станции'
        PROBLEMS = 1, 'Проблемы'

    user = models.ForeignKey('users.CustomUser', on_delete=models.DO_NOTHING, related_name='appeals')
    section = models.PositiveSmallIntegerField(choices=Section.choices)
    message = models.CharField(max_length=255, blank=True)
    phone_number = models.CharField(max_length=20, validators=[phone_validate], blank=True, null=True)

    def __str__(self):
        return f'{self.phone_number} - {self.message[:20]}'



from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError

from apps.users.districts_choices import District
from apps.users.managers import CustomUserManager
from apps.users.validators import phone_validate


class CustomUser(AbstractUser):
    class Regions(models.IntegerChoices):
        SIRDARYO = 1, 'Sirdaryo'
        NAVOIY = 2, 'Navoiy'
        JIZZAX = 3, 'Jizzax'
        XORAZM = 4, 'Xorazm'
        BUXORO = 5, 'Buxoro'
        SURXONDARYO = 6, 'Surxondaryo'
        NAMANGAN = 7, 'Namangan'
        ANDIJON = 8, 'Andijon'
        QASHQADARYO = 9, 'Qashqadaryo'
        SAMARQAND = 10, 'Samarqand'
        FARGONA = 11, 'Fargʻona'
        TOSHKENT = 12, 'Toshkent'
        QORAQALPOGISTON = 13, 'Qoraqalpog‘iston'

    username = None
    objects = CustomUserManager()

    phone_number = models.CharField(max_length=20, unique=True, validators=[phone_validate])
    email = models.EmailField(blank=True, null=True)
    full_name = models.CharField(max_length=150, blank=True, null=True)
    region = models.PositiveSmallIntegerField(choices=Regions.choices, blank= True, null=True)
    district = models.CharField(choices=District.choices, blank=True, null=True) #last
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    USERNAME_FIELD = 'phone_number'

    def clean(self):
        if self.district.split('X')[0] != str(self.region):
            raise ValidationError('District and region do not match')

    def __str__(self):
        return self.phone_number

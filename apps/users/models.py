from django.db import models
from django.contrib.auth.models import AbstractUser

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
        FARGʻONA = 11, 'Fargʻona'
        TOSHKENT = 12, 'Toshkent'

    username = None
    objects = CustomUserManager()

    phone_number = models.CharField(max_length=20, unique=True, validators=[phone_validate])
    email = models.EmailField(unique=True, blank=True, null=True)
    full_name = models.CharField(max_length=150, blank=True, null=True)
    region = models.PositiveSmallIntegerField(choices=Regions.choices, blank= True, null=True)
    district = models.CharField(max_length=150, blank=True, null=True)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    USERNAME_FIELD = 'phone_number'

    def __str__(self):
        return self.phone_number
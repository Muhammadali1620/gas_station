from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Review(models.Model):
    user = models.ForeignKey('users.CustomUser', on_delete=models.SET_NULL, null=True)
    message = models.CharField(max_length=200)

    def __str__(self):
        return self.message[:20]


class UserRating(models.Model):
    user = models.ForeignKey('users.CustomUser', on_delete=models.SET_NULL, null=True)
    station = models.ForeignKey('stations.Station', on_delete=models.CASCADE)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])

    def __str__(self):
        return str(self.rating)
    
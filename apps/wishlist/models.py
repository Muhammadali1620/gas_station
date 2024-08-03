from django.db import models


class WishList(models.Model):
    user = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE)
    station = models.ForeignKey('stations.Station', on_delete=models.CASCADE)
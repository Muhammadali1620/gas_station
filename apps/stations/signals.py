from django.dispatch import receiver
from django.db.models.signals import post_save

from apps.stations.models import StationRating
from django.db.models import Avg


@receiver(post_save, sender=StationRating)
def update_station_rating(instance, created, *args, **kwargs):
    if created:
        instance.station.rating = StationRating.objects.filter(station=instance.station).aggregate(avg_rating=Avg('rating'))['avg_rating']
        instance.station.save()
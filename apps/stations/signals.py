from django.dispatch import receiver
from django.db.models.signals import post_delete
from apps.general.services import delete_file_after_delete_obj
from apps.stations.models import Station, StationImage


@receiver(post_delete, sender=Station)
def delete_photo_on_delete_station(instance, *args, **kwargs):
    delete_file_after_delete_obj(instance)


@receiver(post_delete, sender=StationImage)
def delete_photo_on_delete_station_image(instance, *args, **kwargs):
    delete_file_after_delete_obj(instance)
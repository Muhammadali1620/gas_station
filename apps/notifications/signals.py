from django.dispatch import receiver
from django.db.models.signals import post_delete
from apps.general.services import delete_file_after_delete_obj
from apps.notifications.models import NotificationType


@receiver(post_delete, sender=NotificationType)
def delete_photo_on_delete_notification_type(instance, *args, **kwargs):
    delete_file_after_delete_obj(instance)
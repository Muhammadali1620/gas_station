from django.db import models
from django.conf import settings


class NotificationType(models.Model):
    class Type(models.IntegerChoices):
        DISCOUNT = 1, 'Discount'
        ON_BOOKING = 2, 'On Booking'
        REMINDER = 3, 'Reminder'

    section = models.PositiveSmallIntegerField(choices=Type.choices, unique=True)
    image = models.ImageField(upload_to='notifications/images/')


class Notifications(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='notifications')

    title = models.CharField(max_length=255)
    content = models.CharField(max_length=255)
    section = models.PositiveSmallIntegerField(choices=NotificationType.Type.choices)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
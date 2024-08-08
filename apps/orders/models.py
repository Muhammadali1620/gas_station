from django.utils.timezone import now
from django.db import models
from django.conf import settings
from django.core.exceptions import ValidationError

from apps.general.models import General


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    amount = models.FloatField() 
 
    is_paid = models.BooleanField(default=False)

    paid_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def clean(self):
        if self.pk and self.amount < General.get_min_payment_amount():
            raise ValidationError('Amount must be greater than {}'.format(General.get_min_payment_amount()))
        
    def save(self, *args, **kwargs):
        if self.is_paid and not self.paid_at:
            self.paid_at = now()
        return super().save(*args, **kwargs)
from django.db import models
from django.core.cache import cache


class General(models.Model):
    booking_price = models.PositiveIntegerField(default=0)
    min_payment_amount = models.PositiveIntegerField()
    booking_extra_time = models.PositiveSmallIntegerField()

    @classmethod
    def get_min_payment_amount(cls):
        amount = cache.get('min_payment_amount', None)
        if amount is None:
            amount = getattr(cls.objects.first(), 'min_payment_amount', 5000)
            cache.set('min_payment_amount', amount, 7 * 24 * 60 * 60)
        return amount

    @classmethod
    def get_booking_price(cls):
        amount = cache.get('booking_price', None)
        if amount is None:
            amount = getattr(cls.objects.first(), 'booking_price', 5000)
            cache.set('booking_price', amount, 7 * 24 * 60 * 60)
        return amount

    @classmethod
    def get_booking_extra_time(cls):
        amount = cache.get('booking_extra_time', None)
        if amount is None:
            amount = getattr(cls.objects.first(), 'booking_extra_time', 10)
            cache.set('booking_extra_time', amount, 7 * 24 * 60 * 60)
        return amount

from rest_framework import serializers, exceptions
from apps.booking.models import Booking


class BookingSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    def validate_car(self, car):
        user = self.context['request'].user
        if not user.usercar_set.filter(id=car.id).exists():
            raise exceptions.ValidationError("You don't have this car")
        return car

    class Meta:
        model = Booking
        fields = ['station_petrol_mark', 'car', 'quantity', 'booking_time', 'user']

from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated

from apps.booking.models import Booking
from apps.booking.serializers import BookingSerializer
from apps.booking.permissions import CheckUserBalance


class BookingCreateAPIView(CreateAPIView):
    permission_classes = (IsAuthenticated, CheckUserBalance,)

    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
from rest_framework import serializers

from apps.stations.serializers import StationListSerializer
from apps.wishlist.models import Wishlist


class WishlistSerializer(serializers.ModelSerializer):
    station = StationListSerializer(read_only=True)

    class Meta:
        model = Wishlist
        fields = '__all__'

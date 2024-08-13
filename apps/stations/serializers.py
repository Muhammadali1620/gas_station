from rest_framework import serializers

from apps.stations.models import Station


class StationListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Station
        exclude = ('short_text_uz', 'short_text_en', 'short_text_ru', 'address_uz', 'address_en', 'address_ru')
from rest_framework.generics import ListAPIView

from apps.stations.models import Station
from apps.stations.serializers import StationListSerializer


class StationListAPIView(ListAPIView):
    serializer_class = StationListSerializer
    queryset = Station.objects.all()
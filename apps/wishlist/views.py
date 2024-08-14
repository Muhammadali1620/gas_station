from django.shortcuts import get_object_or_404

from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from apps.wishlist.models import Wishlist
from apps.wishlist.serializers import WishlistSerializer


class WishlistCreateOrDelateAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, pk):
        status = 201
        message = "wishlist created"
        user_id = request.user.id
        get_object_or_404(Wishlist, station_id=pk)
        wishlist, created = Wishlist.objects.get_or_create(user_id=user_id, station_id=pk)
        if not created:
            message = "wishlist deleted"
            wishlist.delete()
            status = 200
        return Response({'message':message}, status=status)
    

class WishlistListAPIView(ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = WishlistSerializer
    
    def get_queryset(self):
        return Wishlist.objects.filter(user_id=self.request.user.id)
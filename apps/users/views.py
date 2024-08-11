from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404

from rest_framework.views import APIView
from rest_framework.response import Response

from apps.users.serializers import UserProfileSerializer


class UserRetrieveUpdateAPIView(APIView):
    def get(self, request):
        user = get_object_or_404(get_user_model(), pk=request.user.id)
        serializer = UserProfileSerializer(user)
        return Response(serializer.data, status=200)

    def put(self, request):
        user = get_object_or_404(get_user_model(), pk=request.user.id)
        serializer = UserProfileSerializer(user, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=100)

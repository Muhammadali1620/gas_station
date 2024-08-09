from rest_framework.views import APIView
from rest_framework.response import Response

from apps.authentication.serializers import SendAuthCodeSerializer, LoginSerializer


class SendAuthCodeAPIView(APIView):
    def post(self, request):
        serializer = SendAuthCodeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=200) 


class LoginAPIView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=200)
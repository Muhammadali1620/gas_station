from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from apps.authentication.serializers import SendAuthCodeSerializer


class SendAuthCodeAPIView(APIView):
    def post(self, request):
        serializer = SendAuthCodeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=200) 

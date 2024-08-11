from rest_framework.views import APIView
from rest_framework.response import Response

from apps.authentication.serializers import ChangePasswordSerializer, PasswordLoginSerializer, SendAuthCodeSerializer, CodeLoginSerializer


class SendAuthCodeAPIView(APIView):
    permission_classes = ()
    def post(self, request):
        serializer = SendAuthCodeSerializer(data=request.data, context={'request':request, 'created':True})
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=200) 


class CodeLoginAPIView(APIView):
    permission_classes = ()
    def post(self, request):
        serializer = CodeLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=200)
    

class PasswordLoginAPIView(APIView):
    permission_classes = ()
    def post(self, request):
        serializer = PasswordLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=200)


class SendChangePasswordCodeAPIView(APIView):
    permission_classes = ()
    def post(self, request):
        serializer = SendAuthCodeSerializer(data=request.data, context={'request':request, 'created':False})
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=200)


class ChangePasswordAPIView(APIView):
    permission_classes = ()
    def post(self, request):
        serializer = ChangePasswordSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=200)
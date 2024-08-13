from rest_framework.views import APIView
from rest_framework.response import Response

from apps.authentication.serializers import (ChangePasswordSerializer, 
                                             LoginSerializer, 
                                             SendAuthCodeSerializer, 
                                             VerifyCodeSerializer,
                                             RegisterSerializer,
                                             SendChangePasswordCodeSerializer)


class RegisterSendCodeAPIView(APIView):
    permission_classes = ()
    authentication_classes = ()

    def post(self, request):
        serializer = SendAuthCodeSerializer(data=request.data, context={'request':request})
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=200) 
    

class VerifyCodeAPIView(APIView):
    permission_classes = ()
    authentication_classes = ()

    def post(self, request):
        serializer = VerifyCodeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=200) 


class RegisterAPIView(APIView):
    permission_classes = ()
    authentication_classes = ()

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=200) 
    

class LoginAPIView(APIView):
    permission_classes = ()
    authentication_classes = ()

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=200)


class SendChangePasswordCodeAPIView(APIView):
    permission_classes = ()
    authentication_classes = ()

    def post(self, request):
        serializer = SendChangePasswordCodeSerializer(data=request.data, context={'request':request})
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=200)


class ChangePasswordAPIView(APIView):
    permission_classes = ()
    authentication_classes = ()
    
    def post(self, request):
        serializer = ChangePasswordSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=200)
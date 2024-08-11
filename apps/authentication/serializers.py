import random

from django.core.cache import cache
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404

from rest_framework import serializers, exceptions
from rest_framework.authtoken.models import Token

from apps.users.validators import phone_validate


class SendAuthCodeSerializer(serializers.Serializer):
    phone_number = serializers.CharField(max_length=13, min_length=13, validators=[phone_validate])
    code = serializers.IntegerField(read_only=True)

    @staticmethod
    def send_code(phone_number, code):
        print('sended')

    @staticmethod
    def check_limit(ip_address):
        if cache.get(ip_address, 0) >= 3:
            raise exceptions.PermissionDenied('try after one hour')

    @staticmethod
    def generate_code():
        return random.randint(1000, 9999)

    def validate(self, attrs):
        attrs = super().validate(attrs)

        request = self.context.get('request')
        ip_address = request.META.get('REMOTE_ADDR')
        phone_number = attrs['phone_number']

        obj = get_user_model().objects.filter(phone_number=phone_number)
        if obj.exists() and self.context['created']:
            raise serializers.ValidationError('Пользователь с таким номером уже существует')
        
        if not obj.exists() and not self.context['created']:
            raise serializers.ValidationError('Пользователь с таким номером не существует')

        attrs['code'] = self.generate_code()
        self.check_limit(ip_address=ip_address)
        self.send_code(phone_number, attrs['code'])
        limit = cache.get(ip_address, 0)
        cache.set(ip_address, limit + 1, 60 * 60)

        cache.set(phone_number, attrs['code'], 10 * 60)
        return attrs


{
"phone_number":"+998994437104"
}    

    
class CodeLoginSerializer(serializers.Serializer):
    phone_number = serializers.CharField(max_length=13, min_length=13, validators=[phone_validate], write_only=True)
    password = serializers.CharField(max_length=128, write_only=True)
    code = serializers.IntegerField(write_only=True)
    token = serializers.CharField(read_only=True)

    def validate(self, attrs):
        attrs = super().validate(attrs)
        phone_number, code, password = attrs['phone_number'], attrs['code'], attrs['password']
        

        if cache.get(phone_number) != code:
            raise serializers.ValidationError('Неверный номер телефона или код')

        user = get_user_model().objects.create_user(phone_number=phone_number, password=password)

        token = Token.objects.create(user_id=user.id)
        attrs['token'] = token.key
        
        return attrs

   
{
    "phone_number": "+998994437104",
    "code": 3621,
    "password":"qwerty"
}


class PasswordLoginSerializer(serializers.Serializer):
    phone_number = serializers.CharField(max_length=13, min_length=13, validators=[phone_validate], write_only=True)
    password = serializers.CharField(max_length=128, write_only=True)
    token = serializers.CharField(read_only=True)

    def validate(self, attrs):
        attrs = super().validate(attrs)
        phone_number, password = attrs['phone_number'], attrs['password']

        user = get_object_or_404(get_user_model(), phone_number=phone_number)
        if not user.check_password(password):
            raise serializers.ValidationError('Неверный номер телефона или пароль')

        user = user
        token, _ = Token.objects.get_or_create(user_id=user.id)
        attrs['token'] = token.key

        return attrs


{
    "phone_number":"+998994337104",
    "password": "qwerty"
}


class ChangePasswordSerializer(serializers.Serializer):
    phone_number = serializers.CharField(max_length=13, min_length=13, validators=[phone_validate], write_only=True)
    password = serializers.CharField(max_length=128, write_only=True)
    token = serializers.CharField(read_only=True)

    def validate(self, attrs):
        attrs = super().validate(attrs)
        password = attrs['password']

        user = get_object_or_404(get_user_model(), phone_number=attrs['phone_number'])

        user.set_password(password)
        user.save()

        token = Token.objects.get(user_id=user.id)
        attrs['token'] = token.key

        return attrs
    
{
    "phone_number": "+998994437104",
    "code": 6552
}
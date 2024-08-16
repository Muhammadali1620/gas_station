import random

from django.core.cache import cache
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from django.contrib.auth.password_validation import validate_password

from rest_framework import serializers, exceptions
from rest_framework.authtoken.models import Token

from apps.users.validators import phone_validate


class VerifyCodeSerializer(serializers.Serializer):
    phone_number = serializers.CharField(max_length=13, min_length=13, validators=[phone_validate], write_only=True)
    code = serializers.IntegerField(write_only=True)

    def validate(self, attrs):
        attrs = super().validate(attrs)
        phone_number, code = attrs['phone_number'], attrs['code']

        if cache.get(f'{phone_number}_auth_code') != code:
            raise serializers.ValidationError('Неверный номер телефона или код')

        return attrs


class RegisterSerializer(VerifyCodeSerializer):
    password = serializers.CharField(max_length=128, validators=[validate_password], write_only=True)
    token = serializers.CharField(read_only=True)

    def validate(self, attrs):
        attrs = super().validate(attrs)
        phone_number, password = attrs['phone_number'], attrs['password']

        user = get_user_model().objects.create_user(phone_number=phone_number, password=password)

        token = Token.objects.create(user_id=user.id)
        attrs['token'] = token.key

        cache.delete(f'{phone_number}_auth_code')

        return attrs


class SendAuthCodeSerializer(serializers.Serializer):
    phone_number = serializers.CharField(max_length=13, min_length=13, validators=[phone_validate])
    code = serializers.IntegerField(read_only=True)

    @staticmethod
    def send_code(phone_number, code):
        print('sended')

    def check_limit(self):
        # checking limit for ip address
        request = self.context.get('request')
        ip_address = request.META.get('REMOTE_ADDR')

        limit = cache.get(ip_address, 0)
        if limit >= 3:
            raise exceptions.PermissionDenied('try after one hour')
        else:
            cache.set(ip_address, limit + 1, 60 * 60)      

    @staticmethod
    def generate_code():
        return random.randint(1000, 9999)

    def validate_phone_number(self, phone_number):
        if get_user_model().objects.filter(phone_number=phone_number).exists():
            raise serializers.ValidationError('Пользователь с таким номером уже существует')
        return phone_number

    def validate(self, attrs):
        attrs = super().validate(attrs)
        phone_number = attrs['phone_number']

        self.check_limit()

        attrs['code'] = self.generate_code()
        self.send_code(phone_number, attrs['code'])
        cache.set(f'{phone_number}_auth_code', attrs['code'], 10 * 60)

        return attrs


class LoginSerializer(serializers.Serializer):
    phone_number = serializers.CharField(max_length=13, min_length=13, validators=[phone_validate], write_only=True)
    password = serializers.CharField(max_length=128, write_only=True)
    token = serializers.CharField(read_only=True)

    def validate(self, attrs):
        attrs = super().validate(attrs)
        phone_number, password = attrs['phone_number'], attrs['password']

        user = get_object_or_404(get_user_model(), phone_number=phone_number)
        if not user.check_password(password):
            raise serializers.ValidationError('Неверный номер телефона или пароль')

        token, _ = Token.objects.get_or_create(user_id=user.id)
        attrs['token'] = token.key

        return attrs
    

class SendChangePasswordCodeSerializer(serializers.Serializer):
    phone_number = serializers.CharField(max_length=13, min_length=13, validators=[phone_validate])
    code = serializers.IntegerField(read_only=True)

    def validate_phone_number(self, phone_number):
        if not get_user_model().objects.filter(phone_number=phone_number).exists():
            raise serializers.ValidationError('Пользователь с таким номером не существует')
        return phone_number
    
    def check_limit(self):
        # checking limit for ip address
        request = self.context.get('request')
        ip_address = request.META.get('REMOTE_ADDR')

        limit = cache.get(ip_address, 0)
        if limit >= 3:
            raise exceptions.PermissionDenied('try after one hour')
        else:
            cache.set(ip_address, limit + 1, 60 * 60)    
    
    def validate(self, attrs):
        attrs = super().validate(attrs)
        phone_number = attrs['phone_number']

        self.check_limit()

        attrs['code'] = SendAuthCodeSerializer.generate_code()
        SendAuthCodeSerializer.send_code(phone_number, attrs['code'])
        cache.set(f'{phone_number}_change_password_code', attrs['code'], 10 * 60)

        return attrs


class ChangePasswordSerializer(serializers.Serializer):
    phone_number = serializers.CharField(max_length=13, min_length=13, validators=[phone_validate], write_only=True)
    password = serializers.CharField(max_length=128, write_only=True, validators=[validate_password])
    code = serializers.IntegerField(write_only=True)
    token = serializers.CharField(read_only=True)

    def validate(self, attrs):
        attrs = super().validate(attrs)
        password = attrs['password']
        phone_number = attrs['phone_number']
        code = attrs['code']

        if cache.get(f'{phone_number}_change_password_code') != code:
            raise serializers.ValidationError('Неверный номер телефона или код')

        user = get_object_or_404(get_user_model(), phone_number=attrs['phone_number'])

        user.set_password(password)
        user.save()

        token, _ = Token.objects.get_or_create(user_id=user.id)
        attrs['token'] = token.key

        cache.delete(f'{phone_number}_change_password_code')

        return attrs
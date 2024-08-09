import random

from django.core.cache import cache
from django.contrib.auth import get_user_model

from rest_framework import serializers
from rest_framework.authtoken.models import Token

from apps.users.validators import phone_validate


class SendAuthCodeSerializer(serializers.Serializer):
    phone_number = serializers.CharField(max_length=13, min_length=13, validators=[phone_validate])
    code = serializers.IntegerField(read_only=True)

    def send_code(self, phone_number, code):
        print('sended')

    @staticmethod
    def generate_code():
        return random.randint(1000, 9999)

    def validate(self, attrs):
        attrs = super().validate(attrs)
        phone_number = attrs['phone_number']
        attrs['code'] = self.generate_code()
        self.send_code(phone_number, attrs['code'])

        cache.set(phone_number, attrs['code'], 10 * 60)
        return attrs

{
"phone_number":"+998994437104"
}    

    
class LoginSerializer(serializers.Serializer):
    phone_number = serializers.CharField(max_length=13, min_length=13, validators=[phone_validate], write_only=True)
    code = serializers.IntegerField(write_only=True)
    token = serializers.CharField(read_only=True)

    def validate(self, attrs):
        attrs = super().validate(attrs)
        phone_number, code = attrs['phone_number'], attrs['code']
        if cache.get(phone_number) != code:
            raise serializers.ValidationError('Неверный код')

        user, created = get_user_model().objects.get_or_create(phone_number=phone_number)
        if created:
            user.set_unusable_password()
            user.save()

        token, _ = Token.objects.get_or_create(user_id=user.id)
        attrs['token'] = token.key
        
        return attrs
    
{
    "phone_number": "+998994437104",
    "code": 3621
}
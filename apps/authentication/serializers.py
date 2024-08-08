import random

from rest_framework import serializers

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

        return attrs
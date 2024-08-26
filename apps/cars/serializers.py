from django.contrib.auth import get_user_model

from rest_framework import serializers

from apps.cars.models import UserCar


class UserCarSerializer(serializers.ModelSerializer):
    user_phone_number = serializers.CharField(source='user.phone_number', read_only=True)
    model_name = serializers.CharField(source='model.name', read_only=True)
    class Meta:
        model = UserCar
        fields = ['pk','user_phone_number', 'model_name', 'number', 'model', 'color', 'petrol_mark']
    
    def validate(self, attrs):
        attrs = super().validate(attrs)
        model = attrs['model']

        if not model.parent or not model.parent.parent:
            raise serializers.ValidationError({'model': 'Модель автомобиля не может быть родительской моделью'})
        return attrs
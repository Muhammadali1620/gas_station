from django.contrib.auth import get_user_model

from rest_framework import serializers

from apps.cars.models import UserCar


class UserCarSerializer(serializers.ModelSerializer):
    user_phone_number = serializers.CharField(source='user.phone_number', read_only=True)
    model_name = serializers.CharField(source='model.name', read_only=True)
    class Meta:
        model = UserCar
        fields = ['pk', 'user','user_phone_number', 'model_name', 'number', 'model', 'color', 'petrol_mark']
        extra_kwargs = {
            'user': {'required': False, 'write_only': True},
            'model': {'write_only': True}
        }
    
    def save(self, **kwargs):
        user = get_user_model().objects.get(pk=self.context['user_id'])
        kwargs['user'] = user
        return super().save(**kwargs)
    
    def validate(self, attrs):
        attrs = super().validate(attrs)
        model = UserCar(**attrs)
        model.clean()
        return attrs
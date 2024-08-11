from rest_framework import serializers

from django.contrib.auth import get_user_model


class UserProfileSerializer(serializers.ModelSerializer):
    get_region = serializers.CharField(source='get_region_display', read_only=True)
    get_district = serializers.CharField(source='get_district_display', read_only=True)
    class Meta:
        model = get_user_model()
        fields = ['pk', 'phone_number', 'balance', 'email', 'full_name', 'region', 'district', 'get_region', 'get_district']
        extra_kwargs = {
            'phone_number': {'read_only': True},
            'balance': {'read_only': True},
            'region': {'write_only': True},
            'district': {'write_only': True},
        }
    
    def validate(self, attrs):
        attrs = super().validate(attrs)
        model = get_user_model()(**attrs)
        model.clean()
        return attrs
    
{
    "pk": 1,
    "phone_number": "+998994337104",
    "balance": "0.00",
    "email": "muhammadali@gmail.com",
    "full_name": "Muhammadali Mahamadvaliev",
    "region":2,
    "district": "2X9"
}
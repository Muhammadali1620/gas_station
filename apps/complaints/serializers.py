from rest_framework import serializers
from apps.complaints.models import Complaint


class ComplaintCreateSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Complaint
        exclude = ['viewed', 'viewed_at']

    def validate(self, attrs):
        attrs = super().validate(attrs)
        if bool(attrs.get('station')) + bool(attrs.get('review')) != 1:
            raise serializers.ValidationError('Either station or review must be provided.')
        return attrs

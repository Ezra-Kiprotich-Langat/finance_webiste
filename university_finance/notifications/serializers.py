from rest_framework import serializers
from .models import NotificationPreferenceModel, NotificationModel

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = NotificationModel
        fieds = '__all__'
        read_only_fields = ['created_at']

class NotificationPreferenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = NotificationPreferenceModel
        fields = '__all__'
        
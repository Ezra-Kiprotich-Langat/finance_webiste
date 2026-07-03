from rest_framework import serializers
from .models import ServiceCategoryModel, ServiceCommentModel, ServiceRequestModel

class ServiceCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceCategoryModel
        fields = '__all__'

class ServiceRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceRequestModel
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at']

class ServiceCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model  = ServiceCommentModel
        fields = '__all__'
        read_only_fields = ['created_at']
from rest_framework import serializers
from .models import StudentProfileModel


class StudentProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentProfileModel
        fields = '__all__'
        
from rest_framework import serializers
from .models import SemesterModel, UnitModel,  UnitRegistrationModel


class SemesterSerializer(serializers.ModelSerializer):
    class Meta:
        model = SemesterModel
        fields = '__all__'

class UnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = UnitModel
        fields = '__all__'


class UnitRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = UnitRegistrationModel
        fields = '__all__'
        read_only_fields = ['registered_at']
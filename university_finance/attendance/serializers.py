from rest_framework import serializers
from .models import AttendanceRecordModel

class AttendanceRecordSerializer(serializers.ModelSerializer):
    percentage = serializers.ReadOnlyField()
    exam_eligible = serializers.ReadOnlyField()

    class Meta:
        model = AttendanceRecordModel
        fields = '__all__'
        
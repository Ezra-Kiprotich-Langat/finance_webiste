from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import AttendanceRecordModel
from .serializers import AttendanceRecordSerializer


class AttendanceRecordViewSet(viewsets.ModelViewSet):
    queryset = AttendanceRecordModel.objects.all()
    serializer_class = AttendanceRecordSerializer
    permission_classes = [IsAuthenticated]
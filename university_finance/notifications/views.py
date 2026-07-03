from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import NotificationModel, NotificationPreferenceModel
from .serializers import NotificationSerializer, NotificationPreferenceSerializer


class NotificationViewSet(viewsets.ModelViewSet):
    queryset = NotificationModel.objects.all()
    serializer_class = NotificationSerializer
    permission_classes = [IsAuthenticated]


class NotificationPreferenceViewSet(viewsets.ModelViewSet):
    queryset = NotificationPreferenceModel.objects.all()
    serializer_class = NotificationPreferenceSerializer
    permission_classes = [IsAuthenticated]
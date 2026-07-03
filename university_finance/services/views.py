from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import ServiceCategoryModel, ServiceRequestModel, ServiceCommentModel
from .serializers import ServiceCategorySerializer, ServiceRequestSerializer, ServiceCommentSerializer

class ServiceCategoryViewSet(viewsets.ModelViewSet):
    queryset = ServiceCategoryModel.objects.all()
    serializer_class = ServiceCategoryModel
    permission_classes = [IsAuthenticated]

class ServiceRequestViewSet(viewsets.ModelViewSet):
    queryset = ServiceRequestModel.objects.all()
    serializer_class = ServiceRequestSerializer
    permission_classes = [IsAuthenticated]

class ServiceCommentViewSet(viewsets.ModelViewSet):
    queryset = ServiceCommentModel.objects.all()
    serializer_class = ServiceCommentSerializer
    permission_classes = [IsAuthenticated]
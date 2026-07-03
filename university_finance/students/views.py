from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import StudentProfileModel
from .serializers import StudentProfileSerializer

class StudentProfileViewSet(viewsets.ModelViewSet):
    queryset = StudentProfileModel.objects.all()
    serializer_class = StudentProfileSerializer
    permission_classes = [IsAuthenticated]
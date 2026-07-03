from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import SemesterModel, UnitModel, UnitRegistrationModel
from .serializers import SemesterSerializer, UnitSerializer, UnitRegistrationSerializer


class SemesterViewSet(viewsets.ModelViewSet):
    queryset = SemesterModel.objects.all()
    serializer_class = SemesterSerializer
    permission_classes = [IsAuthenticated]


class UnitViewSet(viewsets.ModelViewSet):
    queryset = UnitModel.objects.all()
    serializer_class = UnitSerializer
    permission_classes = [IsAuthenticated]

class UnitRegistrationViewSet(viewsets.ModelViewSet):
    queryset = UnitRegistrationModel.objects.all()
    serializer_class = UnitRegistrationSerializer
    permission_classes = [IsAuthenticated]
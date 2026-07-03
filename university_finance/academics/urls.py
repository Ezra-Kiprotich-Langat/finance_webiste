from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SemesterViewSet, UnitViewSet, UnitRegistrationViewSet

router = DefaultRouter()
router.register('semesters', SemesterViewSet)
router.register('units', UnitViewSet)
router.register('unit-registrations', UnitRegistrationViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ServiceCategoryViewSet, ServiceRequestViewSet, ServiceCommentViewSet

router = DefaultRouter()
router.register('çategories', ServiceCategoryViewSet)
router.register('requests', ServiceRequestViewSet)
router.register('comments', ServiceCommentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

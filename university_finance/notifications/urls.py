from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import NotificationViewSet, NotificationPreferenceViewSet

router = DefaultRouter()
router.register('notifications', NotificationViewSet)
router.register('preference', NotificationPreferenceViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

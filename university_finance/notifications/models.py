from django.db import models
from django.conf import settings

NOTIFICATION_TYPES = [
        ('INFO', 'Information'),
        ('WARNING', 'Warning'),
        ('PAYMENT', 'Payment'),
        ('REGISTRATION', 'Registration'),
        ('RESULTS', 'Results'),
        ('SERVICE', 'Service'),
    ]

class NotificationModel(models.Model):
    recipient = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='notifications')
    title = models.CharField(max_length=50)
    message = models.TextField()
    notification_type = models.CharField(max_length=20, choices=NOTIFICATION_TYPES, default='INFO')
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} {self.recipient}"
    
class NotificationPreferenceModel(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='notification_preference')
    email_enabled = models.BooleanField(default=True)
    sms_enabled = models.BooleanField(default=False)
    system_enabled = models.BooleanField(default=True)

    def __Str__(self):
        return f"Preferences for {self.user}"
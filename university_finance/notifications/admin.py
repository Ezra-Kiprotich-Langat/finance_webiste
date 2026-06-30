from django.contrib import admin
from .models import NotificationModel, NotificationPreferenceModel

admin.site.register(NotificationModel)
admin.site.register(NotificationPreferenceModel)

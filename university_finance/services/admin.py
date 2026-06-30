from django.contrib import admin
from .models import ServiceCategoryModel, ServiceRequestModel, ServiceCommentModel

admin.site.register(ServiceCategoryModel)
admin.site.register(ServiceRequestModel)
admin.site.register(ServiceCommentModel)
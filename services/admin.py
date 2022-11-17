from django.contrib import admin
from services.models import ServiceTypeModel, ServiceModel, OrderModel

admin.site.register(ServiceTypeModel)
admin.site.register(ServiceModel)
admin.site.register(OrderModel)

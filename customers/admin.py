from django.contrib import admin
from customers.models import AddressModel, CustomerModel

# Register your models here.

admin.site.register(AddressModel)
admin.site.register(CustomerModel)
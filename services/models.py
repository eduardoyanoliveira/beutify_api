from django.db import models
from customers.models import CustomerModel


class ServiceTypeModel(models.Model):
    name = models.CharField(max_length=70, null=False, blank=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    is_active = models.BooleanField(default=True, null=False, blank=False)

    class Meta:
        db_table = 'tbl_service_types'
        ordering = ('-created_at',)
    
    def __str__(self):
        return self.name


class ServiceModel(models.Model):

    name = models.CharField(max_length=70, null=False, blank=False)
    cost = models.DecimalField(max_digits=7, decimal_places=2)
    price = models.DecimalField(max_digits=7, decimal_places=2)

    type = models.ForeignKey(ServiceTypeModel, on_delete=models.DO_NOTHING)

    is_active = models.BooleanField(default=True, null=False, blank=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'tbl_services'
        ordering = ('-created_at',)
    
    def __str__(self):
        return self.name



class OrderModel(models.Model):

    customer = models.ForeignKey(CustomerModel, on_delete=models.CASCADE)
    service = models.ForeignKey(ServiceModel, on_delete=models.CASCADE)

    schedule_date = models.DateTimeField(auto_now_add=True)
    processing_date = models.DateTimeField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'tbl_orders'
        ordering = ('-created_at',)

    def __str__(self):
        return self.customer.name + " " + self.service.name


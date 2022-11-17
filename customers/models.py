from django.db import models

# Create your models here.


class AddressModel(models.Model):

    street = models.CharField(max_length=250, blank=False, null=False)
    number = models.CharField(max_length=5, blank=False, null=False)
    cep = models.CharField(max_length=8, blank=False, null=False)

    is_active = models.BooleanField(default=True, null=False, blank=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'tbl_adresses'
        ordering = ('-created_at',)
    
    def __str__(self):
        return self.street + ', Nº' + self.number + ' '



class CustomerModel(models.Model):

    name = models.CharField(max_length=80, blank=False, null=False)
    cpf = models.CharField(max_length=11, blank=False, null=False)
    email = models.EmailField(max_length=80, blank=False, null=False)
    phone = models.CharField(max_length=14, blank=False, null=False)

    address = models.CharField(max_length=200, blank=False, null=False)

    is_active = models.BooleanField(default=True, null=False, blank=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'tbl_customers'
        ordering = ('-created_at',)
    
    def __str__(self):
        return self.name

from rest_framework.serializers import ModelSerializer
from customers.models import AddressModel, CustomerModel

class AddressSerializer(ModelSerializer):
    class Meta:
        model = AddressModel
        fields = '__all__'


class CustomerSerializer(ModelSerializer):
    class Meta:
        model = CustomerModel
        fields = '__all__'
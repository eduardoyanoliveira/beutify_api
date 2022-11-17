from rest_framework.viewsets import ModelViewSet
from customers.serializers import AddressSerializer, CustomerSerializer
from customers.models import AddressModel, CustomerModel


class AddressViewSet(ModelViewSet):
    queryset = AddressModel.objects.all()
    serializer_class = AddressSerializer


class CustomerViewSet(ModelViewSet):
    queryset = CustomerModel.objects.all()
    serializer_class = CustomerSerializer
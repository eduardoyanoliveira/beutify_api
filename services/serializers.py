from rest_framework.serializers import ModelSerializer
from services.models import ServiceModel, OrderModel, ServiceTypeModel
from customers.serializers import CustomerSerializer

class ServiceTypeSerializer(ModelSerializer):
    class Meta:
        model = ServiceTypeModel
        fields = '__all__'


class ServiceDetailSerializer(ModelSerializer):
    class Meta:
        depth = 1
        model = ServiceModel
        fields = '__all__'

class ServiceSerializer(ModelSerializer):
    class Meta:
        depth = 1
        model = ServiceModel
        fields = '__all__'

class OrderDetailSerializer(ModelSerializer):

    class Meta:
        depth = 1
        model = OrderModel
        fields = '__all__'


class OrderSerializer(ModelSerializer):

    class Meta:
        model = OrderModel
        fields = '__all__'

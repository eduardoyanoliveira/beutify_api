from services.models import ServiceModel, ServiceTypeModel, OrderModel
from services.serializers import ( 
    ServiceSerializer,
    ServiceDetailSerializer, 
    ServiceTypeSerializer,
    OrderDetailSerializer, 
    OrderSerializer )
from rest_framework.viewsets import ModelViewSet


class ServiceTypeViewSet(ModelViewSet):
    queryset = ServiceTypeModel.objects.all()
    serializer_class = ServiceTypeSerializer


class ServiceViewSet(ModelViewSet):
    queryset = ServiceModel.objects.all()

    def get_serializer_class(self):
        if self.action == 'list' or self.action == 'retrieve':
            return ServiceDetailSerializer
        return ServiceSerializer

class OrderViewSet(ModelViewSet):
    queryset = OrderModel.objects.all()

    def get_serializer_class(self):
        if self.action == 'list' or self.action == 'retrieve':
            return OrderDetailSerializer
        return OrderSerializer

  
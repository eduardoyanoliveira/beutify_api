from rest_framework.routers import DefaultRouter
from services.views import ServiceViewSet, ServiceTypeViewSet, OrderViewSet

app_name = 'services'

router = DefaultRouter()

router.register('service_types', ServiceTypeViewSet, basename='service_types')
router.register('services', ServiceViewSet, basename='services')
router.register('orders', OrderViewSet, basename='orders')


urlpatterns = router.urls
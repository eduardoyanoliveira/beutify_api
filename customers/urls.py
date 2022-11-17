from rest_framework.routers import DefaultRouter
from customers.views import AddressViewSet, CustomerViewSet

app_name = 'customers'

router = DefaultRouter()

router.register('adresses', CustomerViewSet, basename='adresses')
router.register('customers', CustomerViewSet, basename='customers')

urlpatterns = router.urls
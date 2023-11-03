from django.urls import path, include
from rest_framework.routers import DefaultRouter
from events.views.customer import CustomerView
from events.views.contract import ContractView
from events.views.event import EventView

router = DefaultRouter()
router.register('customers', CustomerView, basename='customer')
router.register('customers/(?P<customer_id>[^/.]+)/contracts', ContractView, basename='contract')
router.register('customers/(?P<customer_id>[^/.]+)/contracts/(?P<contract_id>[^/.]+)/events', EventView, basename='event')

urlpatterns = [
    path('', include(router.urls))
]

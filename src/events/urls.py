from django.urls import path, include
from rest_framework.routers import DefaultRouter
from events.views.view_customer import CustomerView
from events.views.view_contract import ContractView
from events.views.view_event import EventView

router = DefaultRouter()
router.register('customers', CustomerView, basename='customer')
router.register('customers/(?P<customer_id>[^/.]+)/contracts', ContractView, basename='contract')
router.register('customers/(?P<customer_id>[^/.]+)/contracts/(?P<contract_id>[^/.]+)/events',
                EventView, basename='event')

urlpatterns = [
    path('', include(router.urls))
]

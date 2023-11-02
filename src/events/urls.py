from django.urls import path, include
from rest_framework.routers import DefaultRouter
from events.views import CustomerView

router = DefaultRouter()
router.register('customers', CustomerView, basename='customer')

urlpatterns = [
    path('', include(router.urls))
]

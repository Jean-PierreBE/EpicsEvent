# Create your views here.
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from events.permissions.perm_customer import OnlyCom
from events.models import Customer
from events.serializers.seri_customer import CustomerSerializer, CustomerUpdSerializer


class CustomerView(viewsets.ModelViewSet):
    serializer_class = CustomerSerializer
    permission_classes = [IsAuthenticated, OnlyCom]

    def get_queryset(self):
        return Customer.objects.all()

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return self.serializer_class
        else:
            return CustomerUpdSerializer

    def perform_create(self, serializer):
        serializer.save(author_user=self.request.user)

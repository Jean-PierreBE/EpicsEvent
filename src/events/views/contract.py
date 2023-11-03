# Create your views here.
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from events.permissions import OnlyCom
from events.models import Customer, Contract
from events.serializers.contract import ContractSerializer, ContractUpdSerializer


class ContractView(viewsets.ModelViewSet):
    serializer_class = ContractSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if self.action == 'retrieve':
            print('retrieve')
        return Contract.objects.all()

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return self.serializer_class
        else:
            return ContractUpdSerializer

    def perform_create(self, serializer):
        serializer.save(customer_id=self.kwargs["customer_id"], author_user=self.request.user)

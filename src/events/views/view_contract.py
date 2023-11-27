# Create your views here.
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from events.permissions.perm_contract import UpdContract
from events.models import Contract
from events.serializers.seri_contract import ContractSerializer, ContractUpdSerializer
from django_filters.rest_framework import DjangoFilterBackend


class ContractView(viewsets.ModelViewSet):
    serializer_class = ContractSerializer
    queryset = Contract.objects.all()
    permission_classes = [IsAuthenticated, UpdContract]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['sign_date', 'amount_contract', 'saldo_contract', 'status_contract']

    def get_queryset(self):
        return self.queryset.filter(customer_id=self.kwargs["customer_id"])

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return self.serializer_class
        else:
            return ContractUpdSerializer

    def perform_create(self, serializer):
        serializer.save(customer_id=self.kwargs["customer_id"], author_user=self.request.user)

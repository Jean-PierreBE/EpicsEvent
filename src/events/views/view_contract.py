# Create your views here.
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from events.permissions.perm_contract import UpdContract
from events.models import Contract
from events.serializers.seri_contract import ContractSerializer, ContractUpdSerializer


class ContractView(viewsets.ModelViewSet):
    serializer_class = ContractSerializer
    permission_classes = [IsAuthenticated, UpdContract]

    def get_queryset(self):
        return Contract.objects.all()

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return self.serializer_class
        else:
            return ContractUpdSerializer

    def perform_create(self, serializer):
        serializer.save(customer_id=self.kwargs["customer_id"], author_user=self.request.user)

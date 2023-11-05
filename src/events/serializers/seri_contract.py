from rest_framework import serializers
from events.models import Contract


class ContractSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contract
        fields = "__all__"


class ContractUpdSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contract
        fields = ['id', 'sign_date', 'amount_contract', 'saldo_contract', 'status_contract']

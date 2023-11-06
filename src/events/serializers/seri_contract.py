from rest_framework import serializers
from events.models import Contract
from events.constants import MSG_ERR_CONTRACT


class ContractSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contract
        fields = "__all__"


class ContractUpdSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contract
        fields = ['id', 'sign_date', 'amount_contract', 'saldo_contract', 'status_contract']

    def validate(self, data):

        if data['amount_contract'] < 0 or data['saldo_contract'] < 0:
            print('ERR-NEG')
            raise serializers.ValidationError(MSG_ERR_CONTRACT['ERR-NEG'])
        elif data['saldo_contract'] > data['amount_contract']:
            raise serializers.ValidationError(MSG_ERR_CONTRACT['ERR-SALDO'])
        else:
            return data

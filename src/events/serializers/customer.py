from rest_framework import serializers
from events.models import Customer


class CustomerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Customer
        fields = "__all__"


class CustomerUpdSerializer(serializers.ModelSerializer):

    class Meta:
        model = Customer
        fields = ['id', 'enterprise_name', 'client_name', 'information', 'email', 'phone']

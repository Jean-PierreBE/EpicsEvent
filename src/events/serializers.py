from rest_framework import serializers
from django.db.models import Q
from events.models import Customer, Contract, Event


class CustomerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Customer
        fields = "__all__"
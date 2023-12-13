from rest_framework import serializers
from events.models import Event, Contract, Customer
from events.constants import MSG_ERR_EVENT
from users_api.models import UserProfile
from django.shortcuts import get_object_or_404


class EventSerializer(serializers.ModelSerializer):
    contact_client = serializers.SerializerMethodField()
    client_name = serializers.SerializerMethodField()
    support_contact = serializers.SerializerMethodField()

    class Meta:
        model = Event
        fields = ['client_name', 'contact_client', 'id', 'begin_date', 'begin_hour', 'end_date', 'end_hour', 'location',
                  'notes', 'attendees_count', 'support_contact', 'support_user', 'author_user',
                  'time_created', 'time_modified']

    def get_contact_client(self, obj):
        contract_exist = get_object_or_404(Contract, id=obj.contract_id)
        customer_exist = get_object_or_404(Customer, id=contract_exist.customer_id)
        return customer_exist.client_name, customer_exist.email, str(customer_exist.phone)

    def get_client_name(self, obj):
        contract_exist = get_object_or_404(Contract, id=obj.contract_id)
        customer_exist = get_object_or_404(Customer, id=contract_exist.customer_id)
        return customer_exist.enterprise_name

    def get_support_contact(self, obj):
        user_exist = get_object_or_404(UserProfile, id=obj.support_user_id)
        return user_exist.first_name, user_exist.last_name


class EventUpdSerializer(serializers.ModelSerializer):

    class Meta:
        model = Event
        fields = ['id', 'begin_date', 'begin_hour', 'end_date', 'end_hour', 'location', 'notes',
                  'attendees_count', 'support_user']

    def validate(self, data):
        if data['begin_date'] > data['end_date']:
            raise serializers.ValidationError(MSG_ERR_EVENT['ERR_DATE'])
        elif data['begin_date'] == data['end_date']:
            if data['begin_hour'] > data['end_hour']:
                raise serializers.ValidationError(MSG_ERR_EVENT['ERR_HOUR'])
        user_exist = get_object_or_404(UserProfile, pseudo=data['support_user'])
        if user_exist.role == 'SUP':
            if data['attendees_count'] < 0:
                raise serializers.ValidationError(MSG_ERR_EVENT['ERR_ATT'])
            else:
                return data
        else:
            raise serializers.ValidationError(MSG_ERR_EVENT['ERR_USER'])

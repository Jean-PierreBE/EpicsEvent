from rest_framework import serializers
from events.models import Event
from events.constants import MSG_ERR_EVENT
from users_api.models import UserProfile
from django.shortcuts import get_object_or_404


class EventSerializer(serializers.ModelSerializer):
    client_name = serializers.CharField(read_only=True, source="event.contract.customer.client_name")

    class Meta:
        model = Event
        fields = ['client_name', 'id', 'begin_date', 'begin_hour', 'end_date', 'end_hour', 'location', 'notes',
                  'attendees_count', 'support_user', 'author_user', 'time_created', 'time_modified']


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

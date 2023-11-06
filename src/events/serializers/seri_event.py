from rest_framework import serializers
from events.models import Event
from events.constants import MSG_ERR_EVENT
from users_api.models import UserProfile
from django.shortcuts import get_object_or_404


class EventSerializer(serializers.ModelSerializer):

    class Meta:
        model = Event
        fields = "__all__"


class EventUpdSerializer(serializers.ModelSerializer):

    class Meta:
        model = Event
        fields = ['id', 'client_name', 'email', 'phone', 'begin_date', 'end_date',
                  'location', 'notes', 'attendees_count', 'support_user']

    def validate(self, data):
        user_exist = get_object_or_404(UserProfile, pseudo=data['support_user'])
        if user_exist.role == 'SUP':
            if data['attendees_count'] < 0:
                raise serializers.ValidationError(MSG_ERR_EVENT['ERR-ATT'])
            else:
                return data
        else:
            raise serializers.ValidationError(MSG_ERR_EVENT['ERR-USER'])

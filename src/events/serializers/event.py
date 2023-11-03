from rest_framework import serializers
from events.models import Event


class EventSerializer(serializers.ModelSerializer):

    class Meta:
        model = Event
        fields = "__all__"


class EventUpdSerializer(serializers.ModelSerializer):

    class Meta:
        model = Event
        fields = ['id', 'begin_date', 'end_date', 'location', 'notes', 'attendees_count']
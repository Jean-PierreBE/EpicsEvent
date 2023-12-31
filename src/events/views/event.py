# Create your views here.
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from events.models import Event
from events.serializers.event import EventSerializer, EventUpdSerializer
from events.permissions.event import UpdEvent
from django_filters.rest_framework import DjangoFilterBackend


class EventView(viewsets.ModelViewSet):
    serializer_class = EventSerializer
    queryset = Event.objects.all()
    permission_classes = [IsAuthenticated, UpdEvent]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['begin_date', 'end_date', 'location', 'attendees_count', 'support_user']

    def get_queryset(self):
        return self.queryset.filter(contract_id=self.kwargs["contract_id"])

    def get_serializer_class(self):
        print(self.action)
        if self.action in ('list', 'retrieve'):
            return self.serializer_class
        else:
            return EventUpdSerializer

    def perform_create(self, serializer):
        serializer.save(contract_id=self.kwargs["contract_id"], author_user=self.request.user)

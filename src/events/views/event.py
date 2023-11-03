# Create your views here.
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from events.permissions import OnlyCom
from events.models import Event
from events.serializers.event import EventSerializer, EventUpdSerializer


class EventView(viewsets.ModelViewSet):
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Event.objects.all()

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return self.serializer_class
        else:
            return EventUpdSerializer

    def perform_create(self, serializer):
        serializer.save(contract_id=self.kwargs["contract_id"], author_user=self.request.user)

# Create your views here.
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from events.models import Customer, Contract, Event
from events.serializers import CustomerSerializer

class CustomerView(viewsets.ModelViewSet):
    serializer_class = CustomerSerializer

    def get_queryset(self):
        owncontributor_id = Contributor.objects.filter(author_user=self.request.user).values_list('project_id')
        return Project.objects.filter(id__in=owncontributor_id)

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return ProjectDetailSerializer
        else:
            return ProjectSerializer

    def perform_create(self, serializer):

        customer = serializer.save()
        contributor.author_user = self.request.user
        contributor.role = "CRT"
        contributor.project_id = project.id
        contributor.save()

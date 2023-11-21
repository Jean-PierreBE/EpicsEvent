from rest_framework import viewsets
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from django_filters.rest_framework import DjangoFilterBackend

from users_api import serializers, models, permissions

# Create your views here.


class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating and updating profiles"""
    serializer_class = serializers.UserProfileSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = (IsAuthenticated, permissions.OnlyGes)
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['pseudo', 'first_name', 'last_name', 'email', 'role']

    def get_queryset(self):
        if self.request.user.role == 'GES':
            return models.UserProfile.objects.all()
        else:
            return models.UserProfile.objects.filter(id=self.request.user.id)

class UserLoginApiView(ObtainAuthToken):
    """Handle creating user authentication tokens"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES

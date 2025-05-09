"""Views for User API"""
from rest_framework import generics, authentication, permissions
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from user.serializers import UserSerialzer, AuthTokenSerializer

class CreateUserView(generics.CreateAPIView):
    """Create new User in system"""
    serializer_class = UserSerialzer


class CreateTokenView(ObtainAuthToken):
    """Create new Token for user"""
    serializer_class = AuthTokenSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class ManageUserView(generics.RetrieveUpdateAPIView):
    """Manage the authenticated user"""
    serializer_class = UserSerialzer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        """Retrieve authenticated user"""
        return self.request.user

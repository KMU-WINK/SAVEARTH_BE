from .models import Route
from .serializers import RouteSerializer
from rest_framework import viewsets
from .permissions import IsOwnerOrReadOnly
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend

class RouteViewSet(viewsets.ModelViewSet):
    # authentication_classes = [BasicAuthentication, SessionAuthentication]
    # permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    queryset = Route.objects.all()
    serializer_class = RouteSerializer

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['user_id']

    def perform_create(self, serializer):
        serializer.save(user = self.request.user)
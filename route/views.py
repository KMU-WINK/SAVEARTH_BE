from route.permissions import IsOwnerOrReadOnly
from .models import Route
from .serializers import RouteSerializer
from rest_framework import viewsets, parsers
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend

class RouteViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    queryset = Route.objects.all()
    serializer_class = RouteSerializer

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['user_id']

    def perform_create(self, serializer):
        serializer.save(user = self.request.user)